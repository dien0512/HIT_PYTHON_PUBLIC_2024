n = int(input('Nhập số lượng phần tử của list: '))
my_list = [int(x) for x in input().split()]
if len(my_list) != n:
    print('Hãy nhập lại.')
else:
    x = int(input('Nhập số x từ bàn phím: '))
    dem = 0
    for i in range(n):
        if my_list[i] == x:
            dem += 1
print('Số x xuất hiện', dem ,'lần')
if len(my_list) >= 8:  # Đảm bảo list có đủ phần tử để thay thế
    my_list[2:8] = [8, 5, 4, 0, 1, 3]
else:
    print("List không đủ phần tử để thực hiện thay thế.")

print(my_list)
my_list.sort()
print('Số nhỏ nhất trong dãy là: ',my_list[0])
print('Số lớn nhất trong dãy là: ',my_list[n-1])
y = int(input('Nhập số y từ bàn phím: '))
my_list.insert(0,y)
print(my_list)
Tang = True
Giam = True
for i in range(len(my_list)-1):
    if my_list[i] < my_list[i+1]:
        Giam= False
    if my_list[i] > my_list[i+1]:
        Tang = False
if Tang == True:
    print('TĂNG')
elif Giam == True:
    print("GIẢM")
else:
    print('NO')
new_list = []
sum = 0
for i in range(len(my_list)):
    sum += my_list[i]
    new_list.append(sum)
print(new_list)
new_arr = [94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
new_arr.sort()
print(new_arr)
for i in range(len(new_arr)):
    new_arr[i] = abs(new_arr[i])
print(new_arr)
new_arr.sort()
print(new_arr)