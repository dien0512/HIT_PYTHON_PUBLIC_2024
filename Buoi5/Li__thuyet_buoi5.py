dict = dict() # khai báo một dict rỗng
dict_1 ={
    'name' : 'Sơn',
    'age' : 20,
    'job' : 'Dev'
}
# dict_2 = { x:x**3 for x in range(5)}
# print(dict_2)
# print(dict_1['name'])
# dict_1['email'] = 'dien05122005@gmai.com'
# print(dict_1)
# x = dict_1.pop('name')
# y = dict_1.popitem() # xóa cặp giá trị cuối
# print(dict_1)
# print(y)
# print(x)
# del dict_1['age'] # xóa hẳn 1 cặp key-value
for key in dict_1.keys():
    print(key)
for value in dict_1.values():
    print(value)
for key,value in dict_1.items():
    print(key,value)
