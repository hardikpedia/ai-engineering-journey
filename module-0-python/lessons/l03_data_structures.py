"""0.3 Data structures"""

# list = JS array
nums = [3, 1, 2]
nums.append(4)              # push
last = nums.pop()           # pop
print(nums, last, len(nums))
print(nums[0], nums[-1])    # negative index = from the end
print(nums[1:3])            # slice -> [1, 2]
print(sorted(nums), nums)   # sorted() returns new list; nums.sort() sorts in place

# dict = JS object / Map
user = {"name": "Hardik", "role": "SDE"}
user["city"] = "Gurugram"
print(user["name"])
print(user.get("email"))              # None instead of KeyError
print(user.get("email", "n/a"))       # default value
for key, value in user.items():       # Object.entries(user)
    print(key, "=", value)
print("name" in user)                 # 'name' in user / user.hasOwnProperty

# Spread / merge
merged = {**user, "role": "Senior SDE"}   # { ...user, role: "Senior SDE" }
print(merged)

# tuple = fixed, immutable list (good for returning several values)
point = (10, 20)
x, y = point                          # destructuring: const [x, y] = point
print(x, y)

# set = JS Set
tags = {"ai", "python", "ai"}
print(tags, "ai" in tags)

# Comprehensions = map + filter in one line
squares = [n * n for n in range(5)]                  # [0,1,4,9,16]
evens = [n for n in range(10) if n % 2 == 0]         # filter
name_lengths = {name: len(name) for name in ["ana", "bob"]}
print(squares, evens, name_lengths)

# Unpacking with *rest
first, *rest = [1, 2, 3, 4]           # const [first, ...rest] = ...
print(first, rest)
