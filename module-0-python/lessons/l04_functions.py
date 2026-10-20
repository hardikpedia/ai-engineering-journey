"""0.4 Functions"""
import time
from functools import wraps


def greet(name, greeting="Hello"):          # default parameter
    return f"{greeting}, {name}!"


print(greet("Hardik"))
print(greet("Hardik", greeting="Hi"))       # keyword argument: order doesn't matter


def total(*numbers):                         # like (...numbers) => ...
    return sum(numbers)


def describe(**info):                        # collects keyword args into a dict
    return ", ".join(f"{k}={v}" for k, v in info.items())


print(total(1, 2, 3))
print(describe(model="gpt", temperature=0.2))

# Spread into a call
args = [1, 2]
opts = {"greeting": "Yo"}
print(total(*args), greet("A", **opts))

# lambda = tiny one-expression arrow function
square = lambda n: n * n                     # const square = n => n * n
print(sorted(["ccc", "a", "bb"], key=lambda s: len(s)))


# Gotcha: never use a mutable default like []
def add_item_bad(item, items=[]):            # the SAME list is reused every call
    items.append(item)
    return items


def add_item_good(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item_bad("a"), add_item_bad("b"))   # ['a','b'] ['a','b']  <- surprise
print(add_item_good("a"), add_item_good("b")) # ['a'] ['b']


# Decorator = a function that wraps another function (like a higher-order fn / middleware)
def timed(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} took {(time.perf_counter() - start) * 1000:.2f} ms")
        return result
    return wrapper


@timed                                        # same as: slow_add = timed(slow_add)
def slow_add(a, b):
    time.sleep(0.05)
    return a + b


print(slow_add(2, 3))
