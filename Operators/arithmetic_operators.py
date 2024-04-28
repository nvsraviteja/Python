def arithmetic_operation(num1,num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1/num2
        else:
            return "Division by zero not allowed"
    else:
        return "Invalid Operator"

# Example usage
num1 = 10
num2 = 5
operator = '+'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

operator = '-'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

operator = '*'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")

operator = '/'
result = arithmetic_operation(num1, num2, operator)
print(f"{num1} {operator} {num2} = {result}")
