import pandas as pd
import chardet

import fastavro
from datapeek import errors


def get_filetype_from_path(filepath: str):
    posn_of_last_fullstop = filepath.rfind(".")
    if posn_of_last_fullstop == -1:
        raise errors.DatapeekNoFiletypeError(
            "Could not identify the file type, please try again with a filepath which "
            "ends with a file extension e.g. '/path/to/file.parquet'"
        )
    return filepath[posn_of_last_fullstop + 1 :]


def get_peek_function(filetype: str):
    functions = {
        "parquet": peek_parquet,
        "avro": peek_avro,
    }
    if filetype not in functions.keys():
        raise errors.DatapeekUnknownFiletypeError(
            f"{filetype} is not a supported file type, "
            f"expected one of [{','.join(functions.keys())}]"
        )
    return functions[filetype]


def show_df_key_info(df: pd.DataFrame):
    # print(f'Number of rows: {df.shape[0]}')
    # print(f'Columns ({df.shape[1]}):')
    print("\nPreview: \n")
    print(df)
    cols = {c: df[c].dtype for c in df.columns}
    print(f"\nColumns:")
    for colname, coltype in cols.items():
        print(f"    {colname} ({coltype})")


def peek_parquet(filepath: str):
    df = pd.read_parquet(filepath, engine="pyarrow")
    show_df_key_info(df)


def get_encoding(filepath: str):
    with open(filepath, 'rb') as indata:
        encoding = chardet.detect(indata.read())
    print(f"Encoding detected by chardet as {encoding['encoding']}, "
          f"confidence {encoding['confidence']}")
    return encoding['encoding']

# def get_encoding(filepath: str):
#     """
#     chardet didn't work so let's try figuring out the encoding ourselves
#     """
#     valid_encodings = ['utf-8', 'utf-16', 'utf-32']
#     for e in valid_encodings:
#         try:
#             with open(filepath, encoding=e) as infile:
#                 infile.read()
#             return e
#         except UnicodeError:  # , UnicodeDecodeError:
#             pass  # next valid_encoding
#     raise errors.DatapeekCouldNotDetectEncoding(
#         f"could not identify encoding; tried {','.join(valid_encodings)}"
#     )


def peek_avro(filepath: str):
    # encoding = get_encoding(filepath)
    encoding = 'utf-32'
    with open(filepath, encoding=encoding) as avrofile:
        reader = fastavro.reader(avrofile)
        records = [r for r in reader]
        df = pd.DataFrame.from_records(records)
        show_df_key_info(df)
