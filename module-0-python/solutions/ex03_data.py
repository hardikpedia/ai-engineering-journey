def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.lower().split():
        word = word.strip(".,!?")
        if word:
            counts[word] = counts.get(word, 0) + 1
    return counts


def top_n(counts: dict[str, int], n: int) -> list[tuple[str, int]]:
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:n]


def unique_sorted(items: list[str]) -> list[str]:
    return sorted({item.strip().lower() for item in items if item.strip()})
