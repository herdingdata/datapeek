import click

from datapeek.access_data import get_filetype_from_path, get_peek_function


@click.command()
@click.argument("filepath")
def peek(filepath: str) -> None:
    """Entrypoint for the datapeek command line tool."""
    filetype = get_filetype_from_path(filepath)
    peek_function = get_peek_function(filetype)
    peek_function(filepath)
