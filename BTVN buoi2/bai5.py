n = int(input('Nhập vào một số n: '))
print(f"Dãy các số Armstrong bậc 3 từ 1 đến {n} là:")

for  i in range(1, n + 1,1):
    sum = 0
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if i == sum:
        print(i)
