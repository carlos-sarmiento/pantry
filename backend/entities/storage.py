from __future__ import annotations
from dataclasses import asdict
from enum import StrEnum
from types import NoneType
from typing import Generic, Optional, Type
from tinydb import TinyDB, Query
from tinydb.table import Document
from dacite import from_dict, Config
import strawberry
from datetime import date, datetime, time
from decimal import Decimal
from backend.entities.core import EmptyID, genID, EntTypeVar, EntInterface
from tinydb.queries import QueryLike
from enum import Enum


db = TinyDB(".vscode/db.json", sort_keys=True, indent=4)

Query = Query


def asdict_factory(cls):
    def factory(obj: list[tuple[str, object]]) -> dict:
        d = {}
        for field_name, field_value in obj:
            field_type = type(field_value)
            if field_type not in [
                NoneType,
                strawberry.ID,
                str,
                int,
                float,
                bool,
                date,
                datetime,
                time,
                Decimal,
                list,
                dict,
                StrEnum,
            ]:
                print(f"Trying to save Value of type {field_type}. This is not allowed and value will be dropped")

            if field_name.endswith("_id") and field_value == EmptyID:
                raise ValueError(f"Field: {field_name} cannot be stored with EmptyID")

            if field_value is not None:
                d[field_name] = field_value
        return d

    return factory


class EntLoader(Generic[EntTypeVar]):
    def __init__(self, table_name, data_class: Type[EntTypeVar]):
        self.__table_name = table_name
        self.__data_class = data_class

    def __call__(self, cls) -> EntInterface[EntTypeVar]:
        def to_dict(obj) -> dict:
            return asdict(obj, dict_factory=asdict_factory(cls))

        def gen_instance(data: Document) -> Optional[EntTypeVar]:
            ent = from_dict(data_class=self.__data_class, data=data, config=Config(cast=[Enum]))  # type: ignore
            ent.id = genID(data.doc_id)
            return ent

        class EntImpl(cls, EntInterface[EntTypeVar]):  # type: ignore
            id: strawberry.ID = genID("invalid")

            @classmethod
            def load(cls, id: strawberry.ID) -> Optional[EntTypeVar]:
                if id is None:
                    return None

                table = db.table(cls.__table_name)
                doc = table.get(doc_id=int(id))

                if doc is None:
                    return None

                return gen_instance(doc)

            @classmethod
            def create(cls, ent: EntTypeVar) -> EntTypeVar:
                table = db.table(cls.__table_name)
                data = to_dict(ent)
                data.pop("id")
                doc_id = table.insert(data)

                ent.id = genID(doc_id)
                return ent

            @classmethod
            def query(cls, query: QueryLike | None = None) -> list[EntTypeVar]:
                table = db.table(cls.__table_name)
                if query is None:
                    results = table.all()
                else:
                    results = table.search(query)

                return [i for i in [gen_instance(i) for i in results] if i is not None]

            @classmethod
            def exists(cls, query: QueryLike) -> bool:
                table = db.table(cls.__table_name)
                results = table.search(query)

                return len(results) > 0

            @classmethod
            def update(cls, ent: EntTypeVar, reload: bool = True) -> EntTypeVar:
                table = db.table(cls.__table_name)
                id = int(ent.id)
                data = to_dict(ent)
                data.pop("id")

                table.update(data, doc_ids=[id])

                if reload:
                    load = cls.load(genID(id))
                    assert load is not None
                    return load
                else:
                    return ent

            @classmethod
            def delete(cls, ent: EntTypeVar) -> None:
                table = db.table(cls.__table_name)
                table.remove(doc_ids=[int(ent.id)])

        setattr(EntImpl, "__name__", getattr(cls, "__name__"))
        setattr(EntImpl, "_EntImpl__table_name", self.__table_name)
        setattr(EntImpl, "_EntImpl__data_class", self.__data_class)
        return EntImpl
