import click

from datapeek import describe
from datapeek.access_data import get_df_function, get_filetype_from_filepath, get_files_from_folderpath


@click.command()
@click.option("-s", "--size", is_flag=True)
@click.option("-c", "--columns", is_flag=True)
@click.option("-r", "--recursive", is_flag=True)
@click.argument("filepath")
def peek(filepath: str, size: bool, columns: bool, recursive: bool) -> None:
    """Entrypoint for the datapeek command line tool."""
    if recursive:
        filepaths = get_files_from_folderpath(filepath)
        for fpath in filepaths:
            print('\n\n', fpath, ':')
            peek_at_one(fpath, size, columns)
    else:  # just one
        peek_at_one(filepath, size, columns)


def peek_at_one(filepath: str, size: bool, columns: bool):
    filetype = get_filetype_from_filepath(filepath)
    df_function = get_df_function(filetype)
    df = df_function(filepath)
    if size:
        describe.describe_size(df)
    elif columns:
        describe.describe_columns(df)
    else:
        describe.describe_all_df_key_info(df)
