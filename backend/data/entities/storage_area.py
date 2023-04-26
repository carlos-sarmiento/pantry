from __future__ import annotations
from dataclasses import dataclass
from backend.entities.core import HasID
from backend.entities.graphql import graphql_type
from backend.entities.storage import EntLoader


@graphql_type
@dataclass
class StorageArea(HasID):
    name: str


@EntLoader(table_name="storage_area", data_class=StorageArea)
class EntStorageArea:
    ...
