from __future__ import annotations

import pluggy

from . import hookspecs  # NOQA

NAME = "snowcli"

hookimpl = pluggy.HookimplMarker(NAME)
