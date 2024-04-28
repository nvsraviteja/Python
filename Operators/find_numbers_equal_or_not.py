def check_equality(num1, num2):
    if num1 == num2:
        return "The two numbers are equal."
    else:
        return "The two numbers are not equal."

# Example usage
num1 = int(input("enter value 1:"))
num2 = int(input("enter value 2:"))

result = check_equality(num1, num2)
print(result)
