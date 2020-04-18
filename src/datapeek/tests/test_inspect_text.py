from datapeek import inspect_text


# -------------------------
# get_value_separator_char
# -------------------------
def test__get_value_separator_char__with_comma__gets_comma(mocker):
    contents = ["col1,col2,col3", "1,3,foo"]
    expected_char = ","

    result_char = inspect_text.get_value_separator_char(contents)

    assert result_char == expected_char


def test__get_value_separator_char__with_pipe__gets_pipe(mocker):
    contents = ["col1|col2|col3", "1|3|foo"]
    expected_char = "|"

    result_char = inspect_text.get_value_separator_char(contents)

    assert result_char == expected_char


def test__get_value_separator_char__with_semicolon__gets_semicolon(mocker):
    contents = ["col1;col2;col3", "1;3;foo"]
    expected_char = ";"

    result_char = inspect_text.get_value_separator_char(contents)

    assert result_char == expected_char


# -------------------------
# get_quote_char
# -------------------------
def test__get_quote_char__with_doublequote__gets_doublequote(mocker):
    contents = ['"col1"|"col2"|"col3"', '"1"|"3"|"foo"']
    expected_char = '"'

    result_char = inspect_text.get_quote_char(contents, separator="|")

    assert result_char == expected_char


def test__get_quote_char__with_singlequote__gets_singlequote(mocker):
    contents = ["'col1'|'col2'|'col3'", "'1'|'3'|'foo'"]
    expected_char = "'"

    result_char = inspect_text.get_quote_char(contents, separator="|")

    assert result_char == expected_char


def test__get_quote_char__with_noquote__gets_empty_str(mocker):
    contents = ["col1|col2|col3", "1|3|foo"]
    expected_char = ""

    result_char = inspect_text.get_quote_char(contents, separator="|")

    assert result_char == expected_char
