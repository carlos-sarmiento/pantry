from __future__ import annotations
from typing import Optional
import strawberry
from strawberry import ID, Private
from dataclasses import field

from .storage import Ent, EntBase


@strawberry.type
@Ent(table_name="product_definition")
class EntProductDefinition(EntBase):
    name: str
    barcodes: list[str] = field(default_factory=list)
    picture_url: str | None = None


@strawberry.type
@Ent(table_name="product_instance")
class EntProductInstance(EntBase):
    product_definition_id: Private[ID]
    storage_area_id: Private[ID]
    count: int

    @strawberry.field
    def storage_area(self) -> EntStorageArea:
        return EntStorageArea.load(self.storage_area_id)

    @strawberry.field
    def product_definition(self) -> EntProductDefinition:
        return EntProductDefinition.load(self.product_definition_id)


@strawberry.type
@Ent(table_name="storage_area")
class EntStorageArea(EntBase):
    name: str


@strawberry.type
class RootQuery:
    @strawberry.field
    def product_definition(self, id: ID) -> Optional[EntProductDefinition]:
        return EntProductDefinition.load(id)

    @strawberry.field
    def product_definitions(self) -> list[EntProductDefinition]:
        return EntProductDefinition.query()

    @strawberry.field
    def storage_areas(self) -> list[EntStorageArea]:
        return EntStorageArea.query()

    @strawberry.field
    def products(self) -> list[EntProductInstance]:
        return EntProductInstance.query()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_product_definition(self, name: str) -> EntProductDefinition:
        return EntProductDefinition.create(EntProductDefinition(name=name))

    @strawberry.mutation
    def create_storage_area(self, name: str) -> EntStorageArea:
        return EntStorageArea.create(EntStorageArea(name=name))

    @strawberry.mutation
    def create_product_instance(
        self, product_definition_id: ID, storage_area_id: ID
    ) -> EntProductInstance:
        return EntProductInstance.create(
            EntProductInstance(
                product_definition_id=product_definition_id,
                storage_area_id=storage_area_id,
                count=1,
            )
        )


schema = strawberry.Schema(query=RootQuery, mutation=Mutation)
