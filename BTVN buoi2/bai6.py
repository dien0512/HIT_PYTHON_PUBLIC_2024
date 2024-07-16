n = int(input('Nhập một số n: '))
print(f'Dãy gồm {n} số hoàn hảo đầu tiên là: ')
for number in range(1,n+1):
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            sum += i
    if sum == number:
        print(number)