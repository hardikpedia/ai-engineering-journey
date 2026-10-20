"""0.4 exercises. Run: uv run pytest tests -k ex04"""


def make_counter(start: int = 0):
    """Return a function that returns start+1, start+2, ... on each call.
    Hint: closures need the `nonlocal` keyword to change outer variables."""
    raise NotImplementedError  # TODO


def retry(times: int):
    """Decorator: call the function up to `times` times.
    Return the first successful result; if all attempts fail, raise the last error.

    @retry(3)
    def flaky(): ...
    """
    raise NotImplementedError  # TODO
