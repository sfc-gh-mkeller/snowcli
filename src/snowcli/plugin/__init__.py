from __future__ import annotations

import pluggy
import typer

from . import hookspecs

NAME = "snowcli"

hookimpl = pluggy.HookimplMarker(NAME)

# Create plugin manager and set it up
pm = pluggy.PluginManager(NAME)
pm.add_hookspecs(hookspecs)


def create_default_typer(**kwargs) -> typer.Typer:
    """Function that creates a default typer class with SnowCLI's defaults."""
    t = typer.Typer(
        context_settings={"help_option_names": ["-h", "--help"]},
        **kwargs,
    )
    return t
