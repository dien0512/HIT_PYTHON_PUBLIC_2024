import math

# a)

n = int(input('Nhập một số nguyên dương n: '))
sum1 = 0
sum2 = 0
for i in range(1,2*n+2,2):
    sum1 += i
for i in range(2,2*n+1,2):
    sum2 += i
print('Tổng của dãy só đó là: ', sum1- sum2)

# b)

n = int(input('Nhập số nguyên dương n: '))
sum = 0
for i in range(1,n+1,1):
    sum += 1/i
print('Tổng của dãy số đó là: ', sum)

# c)

a = float(input('Nhập hệ số a: '))
b = float(input('Nhập hệ số b: '))
c = float(input('Nhập hệ số c: '))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + sqrt(delta)) / 2*a
    x2 = (-b + sqrt(delta)) / 2*a
    print('Phương trình có 2 nghiệm phân biệt là: ')
    print('x1 = ', x1)
    print('x2 = ', x2)
elif delta == 0:
    x =  -b / (2*a)
    print('Phương trình có nghiệm kép là: ' , x)
else: 
    print('Phương trình đã cho vô nghiệm.')

