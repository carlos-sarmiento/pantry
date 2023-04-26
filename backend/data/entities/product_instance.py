from __future__ import annotations
from dataclasses import dataclass

from backend.entities.core import EmptyID, HasID
from backend.entities.graphql import graphql_type


from backend.entities.storage import EntLoader
from strawberry import Private, ID


@graphql_type
@dataclass
class ProductInstance(HasID):
    product_definition_id: Private[ID] = EmptyID
    storage_area_id: Private[ID] = EmptyID
    count: int = 0


@EntLoader(table_name="product_instance", data_class=ProductInstance)
class EntProductInstance:
    ...
