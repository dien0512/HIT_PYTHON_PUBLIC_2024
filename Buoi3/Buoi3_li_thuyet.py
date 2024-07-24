# # # các cách khởi tạo chuỗi

# # my_string = 'Hello'
# # my_string = "Hello"
# # my_string = '''Hello'''
# # my_string = "I ' am"

# #  sử dụng 3 dấu nháy đơn để kéo dài chuỗi thành nhiều dòng

# # my_string = '''Hello, wellcome to the world of Python'''

# s = 'abc\n' # xuống dòng

# # chuỗi trần

# src = r'D:HIT\tbtvn'
# print(src)
# định dạng chuỗi

# # định dạng số nguyên
# s1 =  "Hệ nhị phân của {0} được biểu diễn là {0:b}".format(12)
# print(s1)
# # định dạng số thực
# s2 = "Biểu diễn dưới dạng mũ {0:e}".format(1566.345)
# print(s2)
# # làm tròn số
# s3 = "Một phần ba: {0:.3f}".format(1/3)
# print(s3)
# # căn lề
# s4 = "|{:<10}|{:<10}|{:<10}|".format('list','tuple','set')
# print(s4)

# TOÁN TỬ VÀ CÁC THAO TÁC TRÊN CHUỖI
# duyệt sâu
# s1 ='HIT PYTHON'
# # c1
# for i in s1:
#     print(i, end=" ")
# print()
# # c2
# for i in range(len(s1)):
#     print(s1[i], end=" ")

#print(s1[0:3:1]) # vị trí bắt đầu : vị trí kết thúc : bước nhảy(step)
# có thể bỏ qua các vị trí thì nó sẽ lấy các giá trị mặc định
# lệnh xóa chuỗi là del()
# s = 'HIT PYtHON'
# s = s.lower()
# s1 = 'hit python'
# s2 = 'hit python'
# print(s1)
# print( s1 == s )
# print(id(s))
# print(id(s1))
# print(id(s2))

# list comprehension

# l = [ x for x in range(10)]
# print(l)

# numbers = [int(input()) for _ in range(10)]
# print(numbers)

# vector = [[1,2,3],[4,5,6],[7,8,9]]
# l = []
# for list in vector:
#     for num in list:
#         l.append(num)
# print(l)

# l1 = [num for list in vector for num in list]
# print(l1)

# l2 = [x for x in range(10) if x % 2 == 0]
# print(l2)

# một số ứng dụng của slicing
l = [1,2,3,4]
# # đảo ngược chuỗi
# l1 = l[::-1]
# print(l1)

# sửa
l[1:] = [10,9,8]
print(l)
# chèn
l[:-3] = [10,9,8]
print(l)
# xóa
l[:] = []
print(l)