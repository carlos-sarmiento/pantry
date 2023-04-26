from __future__ import annotations
from backend.data.entities.product_definition import EntProductDefinition, ProductDefinition
from backend.data.entities.product_instance import EntProductInstance, ProductInstance
from backend.data.entities.storage_area import EntStorageArea, StorageArea

from backend.entities.graphql import extended_graphql_field, register_instance_resolver, mutation, query_root
from strawberry import ID


class ProductInstanceExtension(ProductInstance):
    @extended_graphql_field(ProductInstance)
    def storage_area(self) -> StorageArea | None:
        return EntStorageArea.load(self.storage_area_id)

    @extended_graphql_field(ProductInstance)
    def product_definition(self) -> ProductDefinition | None:
        return EntProductDefinition.load(self.product_definition_id)


class ProductInstanceGraphQL:
    @query_root
    def storage_areas(self) -> list[StorageArea]:
        return EntStorageArea.query()

    @mutation
    def create_product_instance(self, product_definition_id: ID, storage_area_id: ID) -> ProductInstance:
        return EntProductInstance.create(
            ProductInstance(
                product_definition_id=product_definition_id,
                storage_area_id=storage_area_id,
                count=1,
            )
        )


register_instance_resolver(entity=ProductInstance, loader=EntProductInstance.load)
