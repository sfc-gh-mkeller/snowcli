from __future__ import annotations

import snowcli
from typer import Typer


@snowcli.hookimpl
def snowcli_add_option(app: Typer) -> None:
    @app.command()
    def hello(name: str | None = None):
        if name is None:
            print("Hello world")
        else:
            print(f"Hello {name}!")
