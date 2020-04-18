from itertools import islice

import chardet


def get_text_file_info(filepath: str):
    """
    determine key info about a text file
    value separator and quote character are determined by looking at the first 1000 lines
    to check whether known characters appear in all of these rows

    :return: encoding, separator_character, quote_character
    """
    encoding = get_encoding(filepath)
    with open(filepath, encoding=encoding) as infile:
        sample_data = list(islice(infile, 1001))
    if sample_data[-1] == "":  # if last line is a newline then let's ignore it
        sample_data = sample_data[:-1]
    separator = get_value_separator_char(sample_data)
    quote_char = get_quote_char(sample_data, separator)
    print(f"Value separator character={separator}\nQuote character={quote_char}")
    return encoding, separator, quote_char


def get_encoding(filepath: str) -> str:
    with open(filepath, "rb") as indata:
        encoding = chardet.detect(indata.read())
    print(
        f"Encoding detected by chardet as {encoding['encoding']}, "
        f"confidence {encoding['confidence']}"
    )
    return encoding["encoding"]


def get_value_separator_char(sample_data: list) -> str:
    """
    attempt a few different separators to determine whether they appear in all the first 1000 lines
    """
    chars_to_try = [",", "|", ";"]
    for char in chars_to_try:
        if all([char in row for row in sample_data]):
            return char


def get_quote_char(sample_data: list, separator: str) -> str:
    """
    attempt a few different quote characters
    to determine whether they appear in all the first 1000 lines
    Note: this won't do well if only some values are quoted
    """
    chars_to_try = ['"', "'"]
    for char in chars_to_try:
        search_for = f"{char}{separator}{char}"
        if all([search_for in row for row in sample_data]):
            return char
    return ""
