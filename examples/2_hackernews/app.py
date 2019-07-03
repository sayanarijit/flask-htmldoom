import json
import os

from flask import Flask
from flask import render_template as render_flask_template
from flask_debugtoolbar import DebugToolbarExtension
from htmldoom import doctype
from htmldoom import elements as e
from htmldoom import render

from flask_htmldoom import render_template as render_htmldoom_template

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "IGNOREME"
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
app.config["DEBUG_TB_PANELS"] = (
    "flask_debugtoolbar.panels.timer.TimerDebugPanel",
    "flask_debugtoolbar.panels.template.TemplateDebugPanel",
    "flask_debugtoolbar.panels.profiler.ProfilerDebugPanel",
    "flask_debugtoolbar.panels.route_list.RouteListDebugPanel",
)
toolbar = DebugToolbarExtension(app)

with open("news.json") as f:
    news = json.load(f)
    newslist = {"news": {i: news for i in range(100)}}


@app.route("/")
def home():
    """Index page - without renderer"""
    return render(
        doctype("html"),
        e.html()(
            e.head()(e.title()("htmldoom rendering framework demo")),
            e.body()(
                e.h1()("Home page"),
                e.a(href="/jinja2")("Jinja2"),
                e.br(),
                e.a(href="/htmldoom")("htmldoom"),
            ),
        ),
    )


@app.route("/jinja2")
def hello_jinja2_view():
    """Jinja2 rendered view"""
    return render_flask_template("index.jinja2", **newslist)


@app.route("/htmldoom")
def hello_htmldoom_view():
    """htmldoom rendered view"""
    return render_htmldoom_template("templates.index", **newslist)


if __name__ == "__main__":
    app.run("0.0.0.0", int(os.environ.get("PORT", "8080")), debug=True)
