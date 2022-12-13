from __future__ import annotations

import pluggy

from . import hookspecs

NAME = "snowcli"

hookimpl = pluggy.HookimplMarker(NAME)

# Create plugin manager and set it up
pm = pluggy.PluginManager(NAME)
pm.add_hookspecs(hookspecs)
