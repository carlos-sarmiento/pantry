from dataclasses import dataclass
from enum import StrEnum
from typing import Callable, Tuple, Type, TypeVar
from backend.entities.core import EntTypeVar

import strawberry

T = TypeVar("T", bound=Callable)
TEntLoader = TypeVar("TEntLoader")

registered_queries: list[Callable] = []
registered_mutations: list[Callable] = []
instance_resolvers: dict[str, Tuple[Type, Callable]] = {}
graphql_types: list[Type] = []


def query_root(func: T) -> T:
    global registered_queries
    func_name = func.__name__
    new = strawberry.field(func)
    registered_queries.append(new)
    new.func_name = func_name  # type: ignore
    return new  # type: ignore


def mutation(func: T) -> T:
    global registered_mutations
    func_name = func.__name__
    new = strawberry.mutation(func)
    registered_mutations.append(new)
    new.func_name = func_name  # type: ignore
    return new  # type: ignore


def extended_graphql_field(klass):
    def decorator(func):
        setattr(klass, func.__name__, strawberry.field(func))
        return func

    return decorator


def graphql_type(cls):
    global graphql_types
    datac = dataclass()(cls)
    graphql_types.append(datac)
    return datac


def register_instance_resolver(entity: Type[EntTypeVar], loader: Callable):
    global instance_resolvers
    instance_resolvers[entity.__name__] = (entity, loader)


def build_mutation_root() -> Type:
    class MutationRoot:
        ...

    for func in registered_mutations:
        setattr(MutationRoot, func.func_name, func)

    return strawberry.type(MutationRoot)


def build_query_root() -> Type:
    global instance_resolvers
    global graphql_types

    for k in graphql_types:
        strawberry.type(k)

    class QueryRoot:
        def node(self, type: str, id: strawberry.ID):
            if type not in instance_resolvers:
                return None

            return instance_resolvers[type][1](id)

    return_types = [i[0] for i in instance_resolvers.values()]

    QueryRoot.node.__annotations__["return"] = strawberry.union("Node", return_types) | None
    QueryRoot.node = strawberry.field()(QueryRoot.node)

    for func in registered_queries:
        setattr(QueryRoot, func.func_name, func)

    return strawberry.type(QueryRoot)


@strawberry.enum
class DeletionResultEnum(StrEnum):
    DELETED = "deleted"
    NOT_FOUND = "not_found"


@strawberry.type
class DeletionResult:
    id: strawberry.ID
    ent_type: strawberry.Private[Type]
    result: DeletionResultEnum

    @strawberry.field
    def type(self) -> str:
        return self.ent_type.__name__
