from __future__ import annotations
from dataclasses import dataclass
from backend.entities.core import EmptyID, HasID
from backend.entities.graphql import graphql_type
from backend.entities.storage import EntLoader
from strawberry import ID, Private


@graphql_type
@dataclass
class ShoppingList(HasID):
    name: str
    store: str | None = None


@EntLoader(table_name="shopping_list", data_class=ShoppingList)
class EntShoppingList:
    ...


@graphql_type
@dataclass
class ShoppingListItem(HasID):
    shopping_list_id: Private[ID] = EmptyID
    product_definition_id: Private[ID] = EmptyID
    amount: int = 1


@EntLoader(table_name="shopping_list_item", data_class=ShoppingListItem)
class EntShoppingListItem:
    ...
