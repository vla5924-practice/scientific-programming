import math


def get_objects():
    data = [
        [],
        dict(),
        1,
        'hi',
        2.1,
        True,
        tuple(),
        set(),
        type,
        None,
        bytearray(),
        bytes(),
        3 + 4j,
        frozenset(),
        range(4, 5),
        reversed('hi'),
        object(),
        property(),
        GeneratorExit(),
        FutureWarning(),
        FloatingPointError(),
        filter(None, 'hi'),
        FileNotFoundError(),
        FileExistsError(),
        Exception(),
        EOFError(),
        EnvironmentError(),
        DeprecationWarning(),
        slice('hi'),
        staticmethod(None),
        zip(),
        classmethod(None),
        map('hi', 'it'),
        memoryview(b'abc'),
        enumerate(b'abc'),
        iter('abc'),
        get_objects,
        ValueError(),
        NameError(),
        TypeError(),
        (x for x in range(1, 2)),
        math,
        str.title,
        iter([]),
        iter({}),
        iter(set()),
        dir,
    ]

    data_types = sorted(data, key=lambda x: str(type(x)))
    return data_types
