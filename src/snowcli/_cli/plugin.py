from __future__ import annotations

import logging
import subprocess
import sys
from typing import Sequence

import typer
from rich.table import Table

from ..plugin import pm
from .util import _print
from .util import console
from .util import exit_with_error

logger = logging.getLogger(__name__)

app = typer.Typer(
    context_settings={"help_option_names": ["-h", "--help"]},
    help="Plugin related actions.",
)


# TODO: add test unit test for these

PYTHON = sys.executable

COMMON_PIP_OPTIONS = (
    "--no-color",
    "--no-input",
)


def run_subprocess(
    cmd: Sequence[str],
    should_log: bool = True,
) -> subprocess.CompletedProcess[str]:
    if should_log:
        cmd_str = " ".join(cmd)
    else:
        cmd_str = "<redacted>"
    logger.debug(f"Going to run {cmd_str} in a subprocess")
    p = subprocess.run(
        cmd,
        capture_output=True,
        encoding="utf-8",
        text=True,
    )
    logger.debug(f"process exited with code: {p.returncode}")
    return p


def run_pip_command(cmd: Sequence[str]) -> subprocess.CompletedProcess[str]:
    return run_subprocess(
        (PYTHON, "-m", "pip", *COMMON_PIP_OPTIONS, *cmd),
    )


@app.command("list")
def list_plugins() -> None:
    """
    List all the installed plugins and their versions
    """
    table = Table("Name", "Version")
    for module, dist in pm.list_plugin_distinfo():
        table.add_row(dist.project_name, dist.version)
    console.print(table)


@app.command("install")
def install_plugin(
    plugin_name: str,
    editable: bool = typer.Option(
        False,
        "-e", "--editable",
        help="Install in editable mode, useful for plugin development",
    ),
) -> None:
    """
    Install a plugin
    """
    other_options = []
    if editable:
        other_options.append("-e")
    p = run_pip_command(
        ("install", *other_options, plugin_name),
    )

    if p.returncode:
        exit_with_error(
            f"While installing '{plugin_name}' encountered following error:\n"
            f"{p.stderr}",
        )
    _print(f"'{plugin_name}' successfully installed")


@app.command("update")
def update_plugin(plugin_name: str) -> None:
    """
    Update a plugin
    """
    p = run_pip_command(
        ("install", "-U", plugin_name),
    )
    if p.returncode:
        exit_with_error(
            f"While updating '{plugin_name}' encountered following error:\n"
            f"{p.stderr}",
        )
    _print(f"'{plugin_name}' successfully updated")


@app.command("remove")
def remove_plugin(plugin_name: str) -> None:
    """
    Remove a plugin
    """
    plugins = list(map(lambda e: e[1].project_name, pm.list_plugin_distinfo()))
    if plugin_name not in plugins:
        exit_with_error(
            f"'{plugin_name}' does not seem to installed",
        )
    p = run_pip_command(
        ("uninstall", "-y", plugin_name),
    )
    if p.returncode:
        exit_with_error(
            f"While removing '{plugin_name}' encountered following error:\n"
            f"{p.stderr}",
        )
    _print(f"'{plugin_name}' successfully removed")
