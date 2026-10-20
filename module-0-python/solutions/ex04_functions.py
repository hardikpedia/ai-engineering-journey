from functools import wraps


def make_counter(start: int = 0):
    count = start

    def increment() -> int:
        nonlocal count          # needed to change a variable from the outer function
        count += 1
        return count

    return increment


def retry(times: int):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last_error = None
            for _ in range(times):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last_error = e
            raise last_error
        return wrapper
    return decorator
