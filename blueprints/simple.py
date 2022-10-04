from sanic import Blueprint, HTTPResponse
from sanic.views import HTTPMethodView
from sanic.response import text, html
from jinja2 import Template
from pathlib import Path
from jinja2.loaders import FileSystemLoader
from jinja2 import Environment


bp = Blueprint("MyInfo", url_prefix="/my", version=1)


@bp.route("/stuff")
async def stuff_handler(request):
    return HTTPResponse("hello world")


class SimpleView(HTTPMethodView):

    def get(self, request, name):
        '''
        http://127.0.0.1:7777/v1/my/class/harrison
        '''
        template = request.app.ctx.env.get_template("index.html")
        return html(
            template.render(
                songs=[
                    "Stairway to Heaven",
                    "Kashmir",
                    "All along the Watchtower",
                    "Black Hole Sun",
                    "Under the Bridge",
                ],
                name = name
            )
        )

    # You can also use async syntax
    async def post(self, request):
        return text("I am post method")

    def put(self, request):
        return text("I am put method")

    def patch(self, request):
        return text("I am patch method")

    def delete(self, request):
        return text("I am delete method")


bp.add_route(SimpleView.as_view(), "/class/<name>")
