my_str = str(input()) 
my_str1 = list(my_str)
print(my_str1)
my_dict = {}
for i in my_str1:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print(my_dict)
