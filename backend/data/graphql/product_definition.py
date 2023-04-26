from __future__ import annotations
from backend.data.entities.product_definition import ProductDefinition, EntProductDefinition, ProductDefinitionSource
from backend.data.entities.shopping_list import EntShoppingListItem, ShoppingListItem
from backend.entities.graphql import (
    DeletionResult,
    DeletionResultEnum,
    extended_graphql_field,
    mutation,
    query_root,
    register_instance_resolver,
)
from backend.entities.storage import Query
from strawberry import ID
import openfoodfacts


class ProductDefinitionExtension(ProductDefinition):
    @extended_graphql_field(ProductDefinition)
    def shopping_list_items(self) -> list[ShoppingListItem]:
        return EntShoppingListItem.query(Query().product_definition_id == self.id)


class ProductDefinitionGraphQLQueries:
    @query_root
    def product_definitions(self, barcodes: list[str] | None = None) -> list[ProductDefinition]:
        query = Query().noop()

        if barcodes:
            query = query & Query().barcodes.any(barcodes)

        return EntProductDefinition.query(query)


class ProductDefinitionGraphQLMutations:
    @mutation
    def create_product_definition(self, name: str) -> ProductDefinition:
        return EntProductDefinition.create(ProductDefinition(name=name, source=ProductDefinitionSource.MANUAL))

    @mutation
    def create_product_definition_from_barcode(self, barcode: str) -> ProductDefinition | None:
        exists = EntProductDefinition.exists(Query().barcodes.any([barcode]))

        if exists:
            raise ValueError("Product barcode already exists")

        result = openfoodfacts.products.get_product(barcode)
        if result["status"] != 1:
            return None

        product = result["product"]

        name = product.get("product_name")
        brand = product.get("brands")
        qty = product.get("quantity")

        if brand is not None:
            name += f" - {brand}"

        if qty is not None:
            name += f" - {qty}"

        return EntProductDefinition.create(
            ProductDefinition(name=name, barcodes=[barcode], source=ProductDefinitionSource.OPEN_FOOD_FACTS)
        )

    @mutation
    def delete_product_definition(self, id: ID) -> DeletionResult:
        product = EntProductDefinition.load(id)

        if product is None:
            return DeletionResult(id=id, ent_type=ProductDefinition, result=DeletionResultEnum.NOT_FOUND)

        EntProductDefinition.delete(product)
        return DeletionResult(id=id, ent_type=ProductDefinition, result=DeletionResultEnum.DELETED)


register_instance_resolver(entity=ProductDefinition, loader=EntProductDefinition.load)
