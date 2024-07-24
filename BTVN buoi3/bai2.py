k = int(input('Nhập số lượng phần tử của list: '))
my_list = [int(x) for x in input().split()]
if len(my_list) != k:
    print('Hãy nhập lại.')
else:
    n = int(input('Nhập vào số dòng của ma trận: '))
    m = int(input('Nhập vào số cột của ma trận: '))
    dem = 0
    new_list = []
    index = 0
    if n * m <= k:
        for i in range(n):
            a = my_list[index:index+m]
            new_list.append(a)
            index += m
    print(new_list)
    else:
    print('NO')
