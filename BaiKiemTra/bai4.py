s = list(map(str, input().split()))
arr = set()
for item in s:
    for char in item:
        if char == " ":
            continue
        arr.add(char)
s1 = set(arr)
print(s1)