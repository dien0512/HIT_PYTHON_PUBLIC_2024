def input_matrix():
    n = int(input('Nhập số hàng của ma trận: '))
    m = int(input('Nhập số cột của ma trận: '))
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        if len(row) != m:
            return "Số lượng phần tử trong hàng không khớp với số cột đã nhập."
        matrix.append(row)
    return matrix, n, m
matrix = input_matrix()
for row in matrix:
        print(row)
print("Ma trận chuyển vị:")
for j in range(m):
    for i in range(n):
        print(matrix[i][j], end=' ')
    print()