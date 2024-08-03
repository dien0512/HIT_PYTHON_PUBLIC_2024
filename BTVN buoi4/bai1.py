my_tuple =("0","1","2","3","4","5","6","7","8","9")
my_tuple_number = tuple(int(s) for s in my_tuple)
print(my_tuple_number)
sum = 0
for i in range(len(my_tuple_number)):
    sum += i
print('Trung bình cộng các số trong tuple là: ', (sum/len(my_tuple_number)))