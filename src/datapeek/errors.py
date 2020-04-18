class DatapeekUnknownFiletypeError(RuntimeError):
    pass

class DatapeekMoreThanOneFiletypeError(RuntimeError):
    pass

class DatapeekNoFiletypeError(RuntimeError):
    pass


class DatapeekCouldNotDetectEncoding(RuntimeError):
    pass
