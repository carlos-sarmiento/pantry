from strawberry.aiohttp.views import GraphQLView

from .graphql.core import schema
from aiohttp import web
from aiohttp.web import Request

routes = web.RouteTableDef()


@routes.get("/")
async def hello(request: Request):
    return web.FileResponse(path="web/static/index.html", status=200)


app = web.Application()
app.add_routes([web.route("*", "/graphql", GraphQLView(schema=schema))])
app.add_routes(routes)

if __name__ == "__main__":
    web.run_app(app)
