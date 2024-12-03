import re

result = 0

with open("input.txt", "r") as f:
    text = f.read()
    pattern = r"mul\(\d+,\d+\)"
    search = re.findall(pattern, text)

    for mul in search:
        nums = re.findall(r"\d+", mul)
        result += int(nums[0]) * int(nums[1])

print(result)


result = 0

with open("input.txt", "r") as f:
    text = f.read()
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    search = re.findall(pattern, text)

    switch = True
    for mul in search:
        if mul == "do()":
            switch = True
        elif mul == "don't()":
            switch = False
        else:
            if switch:
                nums = re.findall(r"\d+", mul)
                result += int(nums[0]) * int(nums[1])

print(result)
