import asyncio
import time

import httpx
import pytest
import respx


# ---------- 0.2
def test_ex02_fizzbuzz(load):
    m = load("ex02_syntax")
    assert m.fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
    assert m.fizzbuzz(15)[-1] == "FizzBuzz"


def test_ex02_grade(load):
    m = load("ex02_syntax")
    assert [m.grade(s) for s in (95, 80, 50, 10)] == ["A", "B", "C", "F"]
    with pytest.raises(ValueError):
        m.grade(101)


# ---------- 0.3
def test_ex03_word_count(load):
    m = load("ex03_data")
    assert m.word_count("Hi hi, there!") == {"hi": 2, "there": 1}


def test_ex03_top_n(load):
    m = load("ex03_data")
    assert m.top_n({"b": 2, "a": 2, "c": 5}, 2) == [("c", 5), ("a", 2)]


def test_ex03_unique_sorted(load):
    m = load("ex03_data")
    assert m.unique_sorted([" AI", "ai", "Python", ""]) == ["ai", "python"]


# ---------- 0.4
def test_ex04_counter(load):
    m = load("ex04_functions")
    c1, c2 = m.make_counter(), m.make_counter(10)
    assert [c1(), c1(), c2()] == [1, 2, 11]


def test_ex04_retry(load):
    m = load("ex04_functions")
    calls = {"n": 0}

    @m.retry(3)
    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise RuntimeError("fail")
        return "ok"

    assert flaky() == "ok" and calls["n"] == 3

    @m.retry(2)
    def always_fails():
        raise ValueError("nope")

    with pytest.raises(ValueError):
        always_fails()


# ---------- 0.5
def test_ex05_budget(load):
    m = load("ex05_classes")
    b = m.TokenBudget(limit=100)
    assert b.spend(30) == 70 and b.remaining == 70
    with pytest.raises(ValueError):
        b.spend(80)
    with pytest.raises(ValueError):
        b.spend(-1)


# ---------- 0.6
def test_ex06_products(load):
    m = load("ex06_pydantic")
    rows = [
        {"name": "Ghee", "price": 650},
        {"name": "", "price": 10},
        {"name": "Pen", "price": -5},
        {"name": "Book", "price": "99.5", "currency": "USD", "tags": ["edu"]},
        {"name": "X", "price": 1, "currency": "EUR"},
    ]
    valid, invalid = m.parse_products(rows)
    assert invalid == 3
    assert [p.name for p in valid] == ["Ghee", "Book"]
    assert valid[0].currency == "INR" and valid[1].price == 99.5


# ---------- 0.7
def test_ex07_json(load, tmp_path):
    m = load("ex07_files")
    target = tmp_path / "nested" / "data.json"
    m.save_json(target, {"a": [1, 2]})
    assert m.load_json(target) == {"a": [1, 2]}
    assert m.load_json(tmp_path / "missing.json", default={}) == {}
    (tmp_path / "bad.json").write_text("{not json")
    assert m.load_json(tmp_path / "bad.json", default=[]) == []


# ---------- 0.9
@respx.mock
async def test_ex09_status_codes(load):
    m = load("ex09_async")
    respx.get("https://x.test/ok").mock(return_value=httpx.Response(200))
    respx.get("https://x.test/missing").mock(return_value=httpx.Response(404))
    respx.get("https://x.test/down").mock(side_effect=httpx.ConnectError("down"))
    async with httpx.AsyncClient() as client:
        codes = await m.fetch_status_codes(
            client, ["https://x.test/ok", "https://x.test/missing", "https://x.test/down"]
        )
    assert codes == [200, 404, 0]


@respx.mock
async def test_ex09_respects_limit(load):
    m = load("ex09_async")
    active = {"now": 0, "max": 0}

    async def slow(request):
        active["now"] += 1
        active["max"] = max(active["max"], active["now"])
        await asyncio.sleep(0.05)
        active["now"] -= 1
        return httpx.Response(200)

    respx.get(url__startswith="https://x.test/").mock(side_effect=slow)
    async with httpx.AsyncClient() as client:
        await m.fetch_status_codes(client, [f"https://x.test/{i}" for i in range(6)], limit=2)
    assert active["max"] == 2
