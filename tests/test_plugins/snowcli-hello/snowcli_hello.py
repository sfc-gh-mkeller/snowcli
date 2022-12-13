from __future__ import annotations

from typing import Optional

import snowcli
import typer


@snowcli.hookimpl
def snowcli_add_option(app: typer.Typer) -> None:
    @app.command()
    def hello(
        name: Optional[str] = typer.Argument(
            None,
            help="name to greet",
        ),
    ):
        """
        Say hi to someone special
        """
        if name is None:
            name = "world"
        print(f"Hello {name}!")
