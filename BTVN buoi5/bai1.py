my_dict = {}
n = int(input("Nhập số lượng cặp khóa-giá trị: "))
for _ in range(n):
    key = input("Nhập khóa: ")
    value = float(input("Nhập giá trị: "))
    my_dict[key] = value
print("Từ điển sau khi nhập dữ liệu:", my_dict)
cnt = 0
for value in my_dict.values():
    if 3.0 <= value <= 3.5:
        cnt += 1
print('Có', cnt, 'sinh viên có điểm tổng kết trong đoạn [3.0, 3.5].')
low_score = []
for key, value in my_dict.items():
    if value < 2.0:
        low_score.append(key)
print("Các khóa có điểm nhỏ hơn 2.0:", low_score)
for key in low_score:
    del my_dict[key] 
print(my_dict)
