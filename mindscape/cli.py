
import click

from mindscape import __version__

def _get_version(ctx: click.Context, param, value):
    if not value or ctx.resilient_parsing:
        return
    print(__version__)
    ctx.exit(0)


@click.group
@click.help_option("-h", "--help")
@click.option(
    "--version",
    is_flag=True,
    is_eager=True,
    expose_value=False,
    callback=_get_version,
    help="Check version and exit.",
)
def main():
    """Mindscape lets you publish Obsidian vaults as good-looking static sites"""
    pass


@main.command("build")
@click.help_option("-h", "--help")
@click.pass_context
def main_build(ctx : click.Context, **_):
    raise NotImplementedError("to be implemented")


@main.command("serve")
@click.help_option("-h", "--help")
@click.pass_context
def main_serve(ctx : click.Context, **_):
    raise NotImplementedError("to be implemented")