def calculate(operation, *args):
    if operation == "add":
        return sum(args)
    elif operation == "multiply":
        result = 1
        for number in args:
            result *= number
        return result
    elif operation == "max":
        return max(args)
    elif operation == "min":
        return min(args)
    else:
        return "Invalid operation"
print(calculate("add", 1, 2, 3, 4))        
print(calculate("multiply", 1, 2, 3, 4))   
print(calculate("max", 1, 2, 3, 4))        
print(calculate("min", 1, 2, 3, 4))        
print(calculate("subtract", 1, 2, 3, 4))   
