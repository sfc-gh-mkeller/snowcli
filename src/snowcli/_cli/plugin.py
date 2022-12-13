from __future__ import annotations

import typer
from rich.table import Table
from typer.rich_utils import _get_rich_console

from ..plugin import pm

app = typer.Typer(
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Plugin related actions",
)


# TODO: add test unit test for these


@app.command("list")
def list_plugins() -> None:
    """
    List all the installed plugins and their versions
    """
    console = _get_rich_console()
    table = Table("Name", "Version")
    for module, dist in pm.list_plugin_distinfo():
        table.add_row(dist.project_name, dist.version)
    console.print(table)
