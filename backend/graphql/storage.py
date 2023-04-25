from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional
from tinydb import TinyDB, Query
from tinydb.table import Document
from dacite import from_dict
import strawberry
from datetime import date, datetime, time
from decimal import Decimal
from abc import ABC

db = TinyDB("db.json")


def genID(val: str | int):
    if type(val) is str:
        return strawberry.ID(val)
    elif type(val) is int:
        return strawberry.ID(str(val))
    else:
        raise ValueError("Invalid Value for ID")


def asdict_factory(cls):
    def factory(obj: list[tuple[str, object]]) -> dict:
        d = {}
        for field_name, field_value in obj:
            if type(field_value) not in [
                strawberry.ID,
                str,
                int,
                float,
                bool,
                date,
                datetime,
                time,
                Decimal,
                None,
                list,
                dict,
            ]:
                continue

            d[field_name] = field_value
        return d

    return factory


@dataclass
class EntBase(ABC):
    id: strawberry.ID = genID("invalid")


class Ent(object):
    def __init__(self, table_name):
        self.__table_name = table_name

    def __call__(self, cls):
        if not issubclass(cls, EntBase):
            raise ValueError(f"Class: {cls} must inherit from EntBase in order " + "to use the @Ent decorator")

        def to_dict(obj) -> dict:
            return asdict(obj, dict_factory=asdict_factory(cls))

        def gen_instance(data: Document) -> Optional[cls]:
            ent = from_dict(data_class=cls, data=data)  # type: ignore
            ent.id = genID(data.doc_id)
            return ent

        @classmethod
        def load(cls, id: strawberry.ID) -> Optional[cls]:
            table = db.table(self.__table_name)
            doc = table.get(doc_id=int(id))

            if doc is None:
                return None

            return gen_instance(doc)

        cls.load = load

        @classmethod
        def create(cls, ent: cls) -> cls:
            table = db.table(self.__table_name)
            data = to_dict(ent)
            data.pop("id")
            doc_id = table.insert(data)

            ent.id = genID(doc_id)
            return ent

        cls.create = create

        @classmethod
        def query(cls, query: Optional[Query] = None) -> list[cls]:
            table = db.table(self.__table_name)
            if query is None:
                results = table.all()
            else:
                results = table.search(query)

            return [gen_instance(i) for i in results]

        cls.query = query

        @classmethod
        def update(cls, ent: cls) -> cls:
            table = db.table(self.__table_name)
            id = int(ent.id)
            data = to_dict(ent)
            data.pop("id")

            table.update(data, doc_ids=[id])

            return cls.load(genID(id))

        cls.update = update

        @classmethod
        def delete(cls, ent: cls) -> None:
            table = db.table(self.__table_name)
            table.remove(doc_ids=[int(ent.id)])

        cls.delete = delete

        return cls
