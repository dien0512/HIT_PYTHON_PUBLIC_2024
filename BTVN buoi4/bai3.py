n, m = map(int, input().split())
array = list(map(int, input().split()))
set_A = set(map(int, input().split()))
set_B = set(map(int, input().split()))
happiness = 0
for number in array:
    if number in set_A:
        happiness += 1
    elif number in set_B:
        happiness -= 1
print(happiness)