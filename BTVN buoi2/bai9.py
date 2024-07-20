# a)

a = int(input('Nhập một số a bất kì: '))
dem = 0
abs_a = abs(a)
while abs_a > 0:
    dem += 1
    abs_a >>= 1
print(f"Số bits cần thiết để biểu diễn {a} là: {dem}")

# b)

x = 'awesome'
print('Python is',x)
print('Pỷthon is {}'.format(x))
print(f'Python is {x}')

# c)

import sys
python_version = sys.version
print(f"Phiên bản Python hiện tại là: {python_version}")