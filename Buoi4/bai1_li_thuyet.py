string = "Hoc lap trinh Python cung HIT"
# ("H", "o", "c",...,"T")
# Dếm số lượng phần tử mà chữ o xuất hiện trong Tuple

#c1:
result1 = []
for char in string:
    if char == " ":
        continue
    result1.append(char)
print("Tuple1  = ", tuple(result1))

#C2:
result2 = []
for index in range(len(string)):
    if string[index] == " ":
        continue
    result2.append(string[index])
print("Tuple2 = ", tuple(result2))
#C3:
result3 = [char for char in string if char is not " "]
print("Tuple3 = " , tuple(result3))

# Đếm
count = 0
occurences_char_o = [count + 1 for char in result3 if char == "o"]
print("o occerences = ", len(occurences_char_o))