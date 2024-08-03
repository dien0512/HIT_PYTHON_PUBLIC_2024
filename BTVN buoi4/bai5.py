n = int(input('Nhập số lượng phần tử của sâu: '))
a = []
for i in range(n):
    s = input()
    a.append(s)
tuple_b = tuple(a)
cnt = 0
print(tuple_b)
for item in tuple_b:
    all_digit = True
    for char in item:
        if char < '0' or char > '9':
            all_digit = False
    if all_digit:
        cnt += 1
print('Có ', cnt, 'phần tử trong b có dạng số')