from __future__ import annotations

from dataclasses import dataclass, field
from enum import StrEnum

from backend.entities.core import HasID
from backend.entities.graphql import graphql_type

from backend.entities.storage import EntLoader

from strawberry import enum


@enum
class ProductDefinitionSource(StrEnum):
    MANUAL = "manual"
    OPEN_FOOD_FACTS = "open_food_facts"


@graphql_type
@dataclass
class ProductDefinition(HasID):
    name: str
    barcodes: list[str] = field(default_factory=list)
    picture_url: str | None = None
    source: ProductDefinitionSource = ProductDefinitionSource.MANUAL


@EntLoader(table_name="product_definition", data_class=ProductDefinition)
class EntProductDefinition(ProductDefinition):
    ...
