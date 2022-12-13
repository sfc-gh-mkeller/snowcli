from __future__ import annotations

from typing import NoReturn

import rich
from typer import Exit

console = rich.console.Console()
err_console = rich.console.Console(stderr=True)


def _print(msg: str) -> None:
    console.print(msg)


def print_error(msg: str) -> None:
    err_console.print(f"[bold red]Error enocuntered:[/bold red]\n{msg}")


def _exit_errorno(errno: int) -> NoReturn:
    raise Exit(code=errno)


def exit_with_error(msg: str, errno: int = 1) -> NoReturn:
    print_error(msg)
    _exit_errorno(errno)
