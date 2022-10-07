from sanic import Blueprint, HTTPResponse
from sanic.views import HTTPMethodView
from sanic.response import text, html


bp = Blueprint("Medium", url_prefix="/medium", version=1)


class SimpleView(HTTPMethodView):

    def get(self, request):
        '''
        http://127.0.0.1:7777/v1/medium/
        '''
        template = request.app.ctx.env.get_template("medium.html")
        return html(
            template.render(body ="MODAL BODY", title = "Modal Title")
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


bp.add_route(SimpleView.as_view(), "/")
