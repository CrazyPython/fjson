import platform
import sys

try:
    if platform.python_implementation() == 'PyPy':
        from json import *
    elif platform.python_implementation() == 'CPython':
        if sys.version_info >= (3, 0):
            from ujson import loads, load
            from rapidjson import dumps, dump
        elif sys.version_info >= (2, 0):
            from ujson import *
    else:
        raise ImportError("You are running an unsupported implementation of Python.")
except ImportError:
    if sys.version_info >= (3, 0):
        raise ImportError("Optimal speed not reached."
                          "ujson and rapidjson are reqired.")
    elif sys.version_info >= (2, 0):
        raise ImportError("Optimal speed not reached."
                          "ujson is required.")
    else:
        raise ImportError("This should never happen.")

del platform
del sys
