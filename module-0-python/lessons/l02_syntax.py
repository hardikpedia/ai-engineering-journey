"""0.2 Syntax vs JS"""

# Variables: no let/const, no semicolons. Names are snake_case.
user_name = "Hardik"
age = 25
is_admin = False          # True/False are capitalised
nothing = None            # Python's null/undefined

# f-strings = template literals
print(f"{user_name} is {age} years old")   # `${userName} is ${age} years old`

# Blocks use indentation (4 spaces) instead of { }
if age >= 18 and not is_admin:             # && -> and, || -> or, ! -> not
    print("adult, not admin")
elif age >= 13:
    print("teen")
else:
    print("child")

# Truthiness: these are all falsy -> 0, "", [], {}, None, False
for value in [0, "", [], {}, None, "hi", [1]]:
    print(repr(value), "->", bool(value))

# Loops: for..of over anything iterable
for i in range(3):          # 0, 1, 2   (like for (let i = 0; i < 3; i++))
    print("i =", i)

for index, name in enumerate(["a", "b"]):   # like arr.forEach((name, index) => ...)
    print(index, name)

count = 0
while count < 2:
    count += 1              # no ++ in Python
print("count", count)

# Equality: == compares value (like ===). `is` checks identity, use it only for None.
print([1, 2] == [1, 2])     # True  (JS would say false!)
print(nothing is None)      # True

# Ternary
label = "adult" if age >= 18 else "minor"   # age >= 18 ? "adult" : "minor"
print(label)

# Integer vs float division
print(7 / 2, 7 // 2, 7 % 2, 2 ** 10)  # 3.5 3 1 1024
