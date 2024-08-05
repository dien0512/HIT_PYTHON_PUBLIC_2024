# Khai bao tuple
# t0 = tuple()
# t1 = ()
# t2 = ("hello" ,1 ,2, ["some text" ,1 ,2])
# t3 = "hello" ,1 ,2, ["some text", 1, 2]
# print(f"t0={t0}\t({type(t0)})")
# print(f"t1={t1}\t({type(t1)})")
# print(f"t2={t2}\t({type(t2)})")
# print(f"t3={t3}\t({type(t3)})")

# print("t2[1]= ", t2[1])
# print("t2[3][2]= ", t2[3][2])
# t2 = list(t2)
# t2[0] = "Hi" # tuple không thể thay đổi được giá trị sau khi gán.
# t2 = tuple(t2)
# print(t2)

# Khai báo một set.

# s = {1,2,6,2,3,4,5}
# # print(s) # khi in ra set các phần tử chỉ lấy duy nhất 1 lần
# # # thêm 1 phần tử vào set
# # s.add(7)
# # print(s)
# # # thêm nhiều phần tử vào set
# s.update([11,127,13,128,3122]) # thêm nhiều phần tử phải đưa vào list hoặc tuple
# print(s)

# # Các câu lệnh xóa một phần tử trong set

# s.remove(2) # xóa 1 phần tử trong set nếu phần tử đó không có thì báo lỗi
# print(s)

# print(s.pop()) # xóa 1 phần tử bất kì và trả lại giá trị của phần tử xóa đó
# print(s)

# s.clear() # xóa tất cả các phần tử

# s.discard() # xóa 1 phần tử trong set nếu phần tử đó không có thì không làm gì

# Các phương thức xác thực

# s1 = {1,2,3,4}
# s2 = {2,3}
# print(s2.issubset(s1)) # kiểm tra xem s2 có phải là tập con của s1
# print(s1.issuperset(s1)) # kiểm tra xem s1 có phải là tập mẹ của s2

# Toán tử và các thao tác trên set

# a = {"blue", "green", "red"}
# b = {"yellow" ,"red", "orange"}
# # Phép hợp
# # Toán tử: |
# s = a | b
# print(s)
# # Phương thức: union()
# s_ = a.union(b)
# print(s_)
#  # Phép giao
# s1 = a & b
# print(s1)
# s2 = a.intersection(b)
# print(s2)
# # Phép hiệu
# s3 = a - b
# print(s3)
# s4 = a.difference(b)
# print(s4)

