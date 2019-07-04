Flask-Htmldoom
================
[htmldoom](https://github.com/sayanarijit/htmldoom) integration for Flask

Checkout the **[live demo](https://htmldoom-flask-example.herokuapp.com/)** with [performance debugging](https://htmldoom-flask-example.herokuapp.com/flask-profiler/)

Usage
----
### Install

```bash
pip install Flask-Htmldoom
```

### Plug into Flask

#### app.py

```python
import os

from flask import Flask

from flask_htmldoom import render_template

app = Flask(__name__)


@app.route("/")
def hello_htmldoom_view():
    """htmldoom rendered view"""
    return render_template("templates.hello", data="Hello htmldoom")


if __name__ == "__main__":
    app.run("0.0.0.0", int(os.environ.get("PORT", "8080")), debug=True)
```

#### templates/hello.py

```python
from htmldoom import elements as e
from htmldoom import renders

from .layout import render_document


@renders(
    e.body()(
        e.h3()("{contents}"),
        e.a(href="/")("Home"),
    )
)
def render_body(data):
    return {"contents": data["data"]}


def render(data):
    return render_document(data, body_renderer=render_body)
```

#### templates/layout.py

```python
from htmldoom import base as b
from htmldoom import elements as e
from htmldoom import render as _render
from htmldoom import renders

doctype = _render(b.doctype("html"))


@renders(e.title()("{doctitle}"))
def render_title(doctitle):
    return {"doctitle": doctitle}


@renders(e.body()("{content}"))
def render_body(data):
    raise NotImplementedError("You are trying to render a layout.")


@renders("{doctype}", e.html()(e.head()("{title}"), "{body}"))
def render_document(
    data,
    title_renderer=render_title,
    body_renderer=render_body,
):
    return {
        "doctype": doctype,
        "title": title_renderer(doctitle=data["data"]),
        "body": body_renderer(data=data),
    }


def render(data):
    return render_document(data=data)
```

Examples
--------
[Find demo and examples here](https://github.com/sayanarijit/flask-htmldoom/blob/master/examples)

### Deploy examples on heroku:

```bash
git push heroku $(git subtree split --prefix examples/2_hackernews master):master
```
