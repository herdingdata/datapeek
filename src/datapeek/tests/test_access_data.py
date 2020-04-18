import pytest

from datapeek import access_data
from datapeek.errors import DatapeekNoFiletypeError, DatapeekUnknownFiletypeError


def test__get_filetype_from_path__with_filetype__identifies_suffix():
    fpath = "/path/to/file.parquet"
    result = access_data.get_filetype_from_path(filepath=fpath)
    assert result == "parquet"


def test__get_filetype_from_path__no_filetype__raises_error():
    fpath = "/path/to/file_no_full_stop_parquet"
    with pytest.raises(DatapeekNoFiletypeError):
        access_data.get_filetype_from_path(filepath=fpath)


def test__get_peek_function__unknown_filetype__raises_error():
    ftype = "notaparquet"
    with pytest.raises(DatapeekUnknownFiletypeError):
        access_data.get_peek_function(filetype=ftype)
