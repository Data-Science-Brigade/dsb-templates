""" <Nome-API> v0.1
"""


__version__ = '0.1'


import inspect


class SingletonArgs(type):
    """ Singleton that keep single instance for single set of arguments. E.g.:
    assert SingletonArgs('spam') is not SingletonArgs('eggs')
    assert SingletonArgs('spam') is SingletonArgs('spam')
    https://gist.github.com/wowkin2/3af15bfbf197a14a2b0b2488a1e8c787
    """

    _instances = {}
    _init = {}

    def __init__(cls, name, bases, dct):
        cls._init[cls] = dct.get("__init__", None)

    def __call__(cls, *args, **kwargs):
        init = cls._init[cls]
        if init is not None:
            key = (
                cls,
                frozenset(inspect.getcallargs(init, None, *args, **kwargs).items()),
            )
        else:
            key = cls

        if key not in cls._instances:
            cls._instances[key] = super(SingletonArgs, cls).__call__(*args, **kwargs)
        return cls._instances[key]
