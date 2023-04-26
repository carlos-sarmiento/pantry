from __future__ import annotations
from strawberry import ID
from tinydb import Query
from backend.data.entities.product_definition import EntProductDefinition, ProductDefinition
from backend.data.entities.shopping_list import EntShoppingList, EntShoppingListItem, ShoppingList, ShoppingListItem
from backend.entities.graphql import extended_graphql_field, mutation, query_root


class ShoppingListExtension(ShoppingList):
    @extended_graphql_field(ShoppingList)
    def items(self) -> list[ShoppingListItem]:
        return EntShoppingListItem.query(Query().shopping_list_id == self.id)


class ShoppingListItemExtension(ShoppingListItem):
    @extended_graphql_field(ShoppingListItem)
    def shopping_list(self) -> ShoppingList | None:
        return EntShoppingList.load(self.shopping_list_id)

    @extended_graphql_field(ShoppingListItem)
    def product_definition(self) -> ProductDefinition | None:
        return EntProductDefinition.load(self.product_definition_id)


class ShoppingListGraphQL:
    @query_root
    def shopping_lists(self) -> list[ShoppingList]:
        return EntShoppingList.query()

    @query_root
    def shopping_list_items(self) -> list[ShoppingListItem]:
        return EntShoppingListItem.query()

    @mutation
    def create_shopping_list(self, name: str) -> ShoppingList:
        return EntShoppingList.create(ShoppingList(name=name))

    @mutation
    def create_shopping_list_item(
        self, shopping_list_id: ID, product_definition_id: ID, amount: int
    ) -> ShoppingListItem:
        return EntShoppingListItem.create(
            ShoppingListItem(
                shopping_list_id=shopping_list_id, product_definition_id=product_definition_id, amount=amount
            )
        )
