"""0.3 exercises. Run: uv run pytest tests -k ex03"""


def word_count(text: str) -> dict[str, int]:
    """Count words, case-insensitive, ignoring . , ! ? at word edges.
    word_count("Hi hi, there!") -> {"hi": 2, "there": 1}"""
    raise NotImplementedError  # TODO


def top_n(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    """Return the n most common (word, count) pairs, highest first.
    Ties are sorted alphabetically."""
    raise NotImplementedError  # TODO


def unique_sorted(items: list[str]) -> list[str]:
    """Trim, lowercase, drop empty strings, remove duplicates, sort.
    [" AI", "ai", "Python", ""] -> ["ai", "python"]"""
    raise NotImplementedError  # TODO
