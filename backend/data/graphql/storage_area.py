from __future__ import annotations

from tinydb import Query
from backend.data.entities.product_instance import EntProductInstance, ProductInstance
from backend.data.entities.storage_area import EntStorageArea, StorageArea
from backend.entities.graphql import extended_graphql_field, mutation, query_root


class StorageAreaExtensions(StorageArea):
    @extended_graphql_field(StorageArea)
    def products(self) -> list[ProductInstance]:
        return EntProductInstance.query(Query().storage_area_id == self.id)


class StorageAreaGraphQL:
    @query_root
    def products(self) -> list[ProductInstance]:
        return EntProductInstance.query()

    @mutation
    def create_storage_area(self, name: str) -> StorageArea:
        return EntStorageArea.create(StorageArea(name=name))
