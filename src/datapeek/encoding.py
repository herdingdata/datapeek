import chardet


def get_encoding(filepath: str) -> str:
    with open(filepath, "rb") as indata:
        encoding = chardet.detect(indata.read())
    print(
        f"Encoding detected by chardet as {encoding['encoding']}, "
        f"confidence {encoding['confidence']}"
    )
    return encoding["encoding"]
