from backend.data.graphql import build_schema
from strawberry.aiohttp.views import GraphQLView

# from strawberry.printer import print_schema

from aiohttp import web
from aiohttp.web import Request

routes = web.RouteTableDef()

schema = build_schema()


@routes.get("/")
async def hello(request: Request):
    return web.FileResponse(path="web/static/index.html", status=200)


# @routes.get("/graphql/schema.graphql")
# @routes.post("/graphql/schema.graphql")
# async def graphql_schema(request: Request):
#     return web.Response(text=print_schema(schema), content_type="application/json")


app = web.Application()
app.add_routes([web.route("*", "/graphql", GraphQLView(schema=schema))])
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app)
