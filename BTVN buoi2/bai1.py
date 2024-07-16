# a)

a = int(input('Nhập vào một số nguyên dương bất kì: '))
sum = 0
while a > 0:
    sum += a % 10
    a //= 10
print('Tổng các chữ số của số nguyên dương đó là: ' , sum)

# b) 

a = int(input('Nhập vào một số nguyên dương bất kì: '))
sum = 0
for i in range(1,a+1,1):
    if a % i == 0:
        sum += i
print('Tổng các ước của số nguyên dương đó là: ', sum)
# c)

a = int(input('Nhập vào cạnh thứ nhất: '))
b = int(input('Nhập vào cạnh thứ hai: '))
c = int(input('Nhập vào cạnh thứ ba: '))
if a + b > c and b + c > a and a + c > b:
    print('Bộ ba số đã nhập thỏa mãn yêu cầu là một tam giác.')
    if a == b and b == c and a == c:
        print('Đây là tam giác đều.')
    elif a**2 + b**2 < c**2 or a**2 + c**2 < b**2 or b**2 + c**2 < a**2:
        print('Đây là tam giác tù.')
    elif a == b or b == c or a == c:
        print('Đây là tam giác cân.')
    elif a**2 + b**2 > c**2 or a**2 + c**2 > b**2 or b**2 + c**2 > a**2:
        print('Đây là tam giác nhọn.')
    elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
        print('Đây là tam giác vuông.')
else:
    print('Bộ ba số đã nhập không thỏa mãn yêu cầu là một tam giác.')