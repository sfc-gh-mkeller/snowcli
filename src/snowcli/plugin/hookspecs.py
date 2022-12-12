from __future__ import annotations

import pluggy
from typer import Typer

hookspec = pluggy.HookspecMarker("snowcli")


@hookspec
def snowcli_add_option(app: Typer) -> None:
    """Have a look at the ingredients and offer your own.

    :param ingredients: the ingredients, don't touch them!
    :return: a list of ingredients
    """
