import click

from datapeek import describe
from datapeek.access_data import get_df_function, get_filetype_from_path


@click.command()
@click.option("-s", "--size", is_flag=True)
@click.option("-c", "--columns", is_flag=True)
@click.argument("filepath")
def peek(filepath: str, size: bool, columns: bool) -> None:
    """Entrypoint for the datapeek command line tool."""
    filetype = get_filetype_from_path(filepath)
    df_function = get_df_function(filetype)
    df = df_function(filepath)
    if size:
        describe.describe_size(df)
    elif columns:
        describe.describe_columns(df)
    else:
        describe.describe_all_df_key_info(df)
