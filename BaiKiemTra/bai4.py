s = list(map(str, input().split()))
s1 = str(s)
arr = []
for i in range(len(s1)):
    if s1[i] == " ":
        continue
    arr.append(s1[i])
s2 = set(arr)
print(arr)
