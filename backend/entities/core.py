from __future__ import annotations
from abc import abstractmethod
from typing import Generic, Optional, Protocol, TypeVar
from tinydb.queries import QueryLike
import strawberry


def genID(val: str | int) -> strawberry.ID:
    if type(val) is str:
        return strawberry.ID(val)
    elif type(val) is int:
        return strawberry.ID(str(val))
    else:
        raise ValueError("Invalid Value for ID")


EmptyID = genID("EmptyID")


@strawberry.type
class HasID:
    id: strawberry.ID = EmptyID


EntTypeVar = TypeVar("EntTypeVar", bound=HasID)


class EntInterface(Protocol, Generic[EntTypeVar]):
    @abstractmethod
    def load(cls, id: strawberry.ID) -> Optional[EntTypeVar]:
        ...

    @abstractmethod
    def create(cls, ent: EntTypeVar) -> EntTypeVar:
        ...

    @abstractmethod
    def query(cls, query: QueryLike | None = None) -> list[EntTypeVar]:
        ...

    @abstractmethod
    def update(cls, ent: EntTypeVar, reload: bool = True) -> EntTypeVar:
        ...

    @abstractmethod
    def delete(cls, ent: EntTypeVar) -> None:
        ...

    @abstractmethod
    def exists(cls, query: QueryLike) -> bool:
        ...
