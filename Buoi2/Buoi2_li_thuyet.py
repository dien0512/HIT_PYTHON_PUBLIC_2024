my_list = [1,2,3,4]
print(type(my_list))
print(my_list[0])

#kieu du lieu tuples
#cu phap
t = (1,2,3)
print(type(t))
#khi khai bao kieu du lieu tuples ma chi co duy nhat 1 phan tu de kieu du lieu no truy xuat la kieu tuples thi can co dau ,
#kieu du lieu dictionary
#cu phap
my_dict = {
    "ten" : "An",
    "gioi tinh" : "Nam",
    "nam sinh" : 2002
} 
print(type(my_dict))
#de khai bao 1 dictionary rong
# my_dict = dict()
# co 3 cach khai bao ham print
a = 5
b = 4
print('a = ', a)
print('{} {}' . format(a,b))
print(f'{a} {b}')
print('Tong :' , f'{a} + {b} = {a + b}')

#cac toan tu so hoc trong Python
a = 5
b = 2
print(f'{a + b}')
print(f'{a - b}')
print(f'{a * b}')
print(f'{a / b}')
#lay phan nguyen
print(f'{a // b}')
#ham mu
print(f'{a ** b}')

x = 5
print(x < 6 and x < 10 )
print( x < 6 or x < 10)
print(not( x < 6 and x < 10))

# kieu toan tu thanh vien
# in : co trong
# not int : khong co trong

a = 5
a += 1
print(a)
# toan tu nhan dang 
a = 5
b = 5
c = 1
print( a is b)
print( a is c)
print( a is not c)
# cu phap cau lenh if
if 5 > 4 :
    print('Yes')
# cu phap cua lenh if else

a = 5
b = 2
c = 1
if a + b > c :
   print('...')
else :
   print(' ')

# nhap vao 3 so nguyen a , b, c
# kiem tra xem 3 so nhap vao co tao thanh 1 tam giac hay khong

for i in range(1,6,2) :
   print(i, end = ' ')
# trong range theo thu tu start, stop, step (bat dau, ket thuc, buoc nhay)
# vong lap while

a = 10
while a > 5:
   print(a, end=' ')
   a -= 1
   continue 
   print('...')

# ham in ea chi so index
#enumerate
a = ['eat', 'sleep', 'repeat']
for idx, val in enumerate(a):
   print(idx,val)
# cau lenh for else    lenh else chi duoc thuc hien khi cau lenh for duoc thuc hien het khi cau lenh for khong thuc hien het thi cau lenh else se khong thuc hien