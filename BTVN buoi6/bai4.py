def sum_digit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
def count_step(n):
    step = 0
    while n >= 10:
        n = sum_digit(n)
        step += 1
    return step + 1, n
n = 123456
steps, result = count_step(n)
print(f"Số bước thực hiện: {steps}")
print(f"Kết quả cuối cùng: {result}")
