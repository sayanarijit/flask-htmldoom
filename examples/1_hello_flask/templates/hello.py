from htmldoom import elements as e
from htmldoom import renders

from .layout import render_document


@renders(
    e.body()(
        e.h3()("{contents}"),
        e.a(href="/")("Home"),
        e.br(),
        e.a(href="/jinja2")("jinja2"),
    )
)
def render_body(data):
    return {"contents": data["data"]}


def render(data):
    return render_document(data, body_renderer=render_body)
