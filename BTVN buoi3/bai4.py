a = input('Nhập một chuỗi văn bản chứa họ và tên của một thành viên trong câu lạc bộ: ')
a1 = a.split()
for i in range(len(a1)):
    a1[i] = a1[i].title()
for i in a1:
    print(i,end=' ')