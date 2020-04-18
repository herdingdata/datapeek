from pprint import pprint as pp

import pandas as pd


def describe_all_df_key_info(df: pd.DataFrame):
    """
    Print all the things we can about a dataframe. The default choice.
    """
    print("\nSize: \n")
    print(f"Number of rows: {df.shape[0]}")
    print(f"Number of columns: {df.shape[1]}")
    print("\nPandas preview: \n")
    print(df)
    describe_columns(df)


def describe_size(df: pd.DataFrame):
    """
    When we just need to know how big it is
    """
    print(f"{df.shape[0]} rows x {df.shape[1]} columns")


def describe_columns(df: pd.DataFrame):
    """
    When we just need to know what's in the columns
    """
    print(f"\nColumns:")
    cols = {c: df[c].dtype for c in df.columns}
    for colname, coltype in cols.items():
        if coltype == "object":
            max_size = max(df[colname].astype(str).apply(len))
            pp((f"{colname}", f"{coltype}", f"max_length={max_size}"))
            # print(f"    {colname}\t({coltype})\tmax_length={max_size}")
        else:
            pp((f"{colname}", f"{coltype}"))
