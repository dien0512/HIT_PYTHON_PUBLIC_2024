n = int(input('Nhập vào số nguyên dương n: '))
x0 = 0
x1 = 1
print(f'Dãy só gồm {n} số fibo đầu tiên là: ')
for i in range(2,n+1,1):
    print(x0, end=" ")
    xn = x0 + x1
    x0 = x1
    x1 = xn
 
    