import random
N = int(input("Nhập số lượng tài khoản sinh viên(10 <= N <= 100000): "))
my_lists = ["CNTT", "KHMT", "KTPM", "HTTT"]
my_dict = {}
for i in range(1,N+1):
    MSV = f"20236{i:05d}"
    my_list = random.choice(my_lists)
    password = f"{my_list}{MSV}"
    account_name = f"Account {i}: "
    my_dict[account_name] = {"Username": MSV, "Password": password}
for account_name, TT in my_dict.items():
    print(f"{account_name}: {TT}")