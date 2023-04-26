import importlib
from os.path import dirname, basename, isfile, join
import glob
from strawberry import Schema
from backend.entities.graphql import build_mutation_root, build_query_root


modules = glob.glob(join(dirname(__file__), "*.py"))
for a in [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith("__init__.py")]:
    importlib.import_module(f"{__package__}.{a}")


def build_schema():
    return Schema(query=build_query_root(), mutation=build_mutation_root())
