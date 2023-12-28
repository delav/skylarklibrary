import inspect


def keyword(name=None):
    """
    Decorator for keyword.
    """
    if inspect.isroutine(name):
        return keyword()(name)

    def decorator(func):
        func.cname = name
        return func

    return decorator
