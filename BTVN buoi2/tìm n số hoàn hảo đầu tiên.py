n = int(input('Nhập một số n: '))
count = 0
number = 1
print('Dãy gồm n số hoàn hảo đầu tiên là: ')
while count < n:
    sum = 0
    for i in range(1,number):
        if number % i == 0:
            sum += i
    if sum == number:
        print(number)
        count += 1
    number += 1