from pydoc import locate

from flask import _app_ctx_stack, before_render_template, template_rendered
from htmldoom import render


class RendererNotFound(Exception):
    """Exception raised when renderer not found."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class HTMLDoomRenderer:
    """The htmldoom renderer."""

    def __init__(self, app=None):
        self.app = None
        if app is not None:
            self.init_app(app)
        self.app = app

    def init_app(self, app):
        if self.app:
            raise RuntimeError(
                "Cannot call init_app when app argument was "
                "provided to HTMLDoomRenderer constructor."
            )


def _render(renderer, context, app):
    """Renders the template and fires the signal"""

    _renderer = locate(renderer)
    if not _renderer:
        raise RendererNotFound(renderer)

    _context = dict(app.jinja_env.globals, **context)
    before_render_template.send(app, template=renderer, context=_context)
    rv = _renderer(_context)
    template_rendered.send(app, template=renderer, context=_context)
    return rv


def render_template(template_name, **context):
    ctx = _app_ctx_stack.top
    ctx.app.update_template_context(context)
    return render(_render(f"{template_name}.render", context, ctx.app))
