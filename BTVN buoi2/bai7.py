n = int(input('Nhập một số n: '))
print(f'Các cặp số Amicable từ 1 đến {n} là: ')
for a in range(1,n+1):
    sum1 = 0
    for i in range(1,a):
        if a % i == 0:
            sum1 += i
    b = sum1
    sum2 = 0
    for j in range(1,n+1):
        if b % j == 0:
            sum2 += j
    if sum2 == a and a != b:
        print(f'({a},{b})')
