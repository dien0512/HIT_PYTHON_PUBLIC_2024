# Cho một danh sách
# In ra phần tử lớn thứ 2 trong danh sách

n = int(input('Nhập số lượng phần tử của list: '))
my_list = [int(x) for x in input().split()]
my_list.sort()
print(my_list[n-2])