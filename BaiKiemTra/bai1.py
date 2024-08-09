my_tuple = tuple(map(int, input().split()))
s = set(my_tuple)
cnt = 0
a = []
for i in s:
    for j in my_tuple:
        if j == i:
            cnt += 1
    if cnt % 5 == 0 and cnt % 10 != 0:
        a.append(j)
for j in a:
    print (j, end=" ")
