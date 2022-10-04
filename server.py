from blueprints.simple import bp as user_bp
from blueprints.medium import bp as medium_bp
from sanic import Sanic
from pathlib import Path
from jinja2.loaders import FileSystemLoader
from jinja2 import Environment

app = Sanic("MyHelloWorldApp")
app.blueprint([user_bp, medium_bp])

@app.before_server_start
def setup_template_env(app, _):
    app.ctx.env = Environment(
        loader=FileSystemLoader(Path(__file__).parent /"templates"),
        autoescape=True,
    )
