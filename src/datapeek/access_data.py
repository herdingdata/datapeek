import fastavro
import pandas as pd
from os import listdir
from os.path import isfile, join
from datapeek import encoding, errors


def get_filetype_from_filepath(filepath: str):
    posn_of_last_fullstop = filepath.rfind(".")
    if posn_of_last_fullstop == -1:
        raise errors.DatapeekNoFiletypeError(
            "Could not identify the file type, please try again with a filepath which "
            "ends with a file extension e.g. '/path/to/file.parquet'"
        )
    return filepath[posn_of_last_fullstop + 1 :]


def get_files_from_folderpath(folderpath: str):
    """
    also validates that all files are in the same extension
    (could be expanded later to not have this requirement, but for now the primary use
    case is a folder of parquet or avro files and nothing else)
    """
    files_in_dir = [join(folderpath, f) for f in listdir(folderpath)
                    if isfile(join(folderpath, f)) and not f.startswith('.')]
    filetypes = set([get_filetype_from_filepath(fpath) for fpath in files_in_dir])
    if len(filetypes) > 1:
        raise errors.DatapeekMoreThanOneFiletypeError(
            "More than one filetype detected in directory. The recursive option can only be "
            "used for a folder which has only files that all have the same type "
            f"(e.g. a folder of parquet files). Filetypes found: {','.join(filetypes)}"
        )
    return files_in_dir


def get_df_function(filetype: str):
    functions = {
        "parquet": get_df_from_parquet,
        "avro": get_df_from_avro,
        "csv": get_df_from_csv,
    }
    filetype = filetype.lower()
    if filetype not in functions.keys():
        raise errors.DatapeekUnknownFiletypeError(
            f"{filetype} is not a supported file type, "
            f"expected one of [{','.join(functions.keys())}]"
        )
    return functions[filetype]


def get_df_from_parquet(filepath: str):
    return pd.read_parquet(filepath, engine="pyarrow")


def get_df_from_avro(filepath: str):
    with open(filepath, "rb") as avrofile:
        reader = fastavro.reader(avrofile)
        records = [r for r in reader]
        return pd.DataFrame.from_records(records)


def get_df_from_csv(filepath: str):
    encode = encoding.get_encoding(filepath)
    return pd.read_csv(filepath, encoding=encode, engine="python")
