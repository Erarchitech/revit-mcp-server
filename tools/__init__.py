# -*- coding: utf-8 -*-
"""MCP tool modules (DeGram read-only fork).

Each module in this package defines ``register_<name>_tools(mcp, ...)`` and
pairs with a route module in ``revit_mcp/``. Only modules that host at least one
allowlisted tool are listed in ``_MODULES``; the other upstream modules stay on
disk but are never imported. Registration additionally goes through
``ReadOnlyToolRegistry``, so a mixed module can only ever register names in
``degram_readonly.ALLOWED_TOOLS`` (phase 1301 D-10).
"""

from importlib import import_module

import degram_readonly

# (module, registration function, HTTP helpers it takes after `mcp`)
_ALL = ("get", "post", "image")
_MODULES = (
    ("status_tools", "register_status_tools", ("get",)),
    ("view_tools", "register_view_tools", _ALL),
    ("model_tools", "register_model_tools", ("get",)),
    ("colors_tools", "register_colors_tools", ("get", "post")),
    ("parameter_tools", "register_parameter_tools", _ALL),
    ("degram_tools", "register_degram_tools", ("get", "post")),
)


def register_tools(mcp_server, revit_get, revit_post, revit_image):
    """Register the allowlisted tools with ``mcp_server``."""
    guarded = degram_readonly.ReadOnlyToolRegistry(mcp_server)
    helpers = {
        "get": degram_readonly.structured_helper(revit_get),
        "post": degram_readonly.structured_helper(revit_post),
        "image": revit_image,
    }
    for module_name, func_name, needs in _MODULES:
        register = getattr(import_module("." + module_name, __name__), func_name)
        register(guarded, *(helpers[n] for n in needs))
