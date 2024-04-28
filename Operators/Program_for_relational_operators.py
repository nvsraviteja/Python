def compare_numbers(num1, num2):
    if num1 < num2:
        print(f"{num1} is less than {num2}")
    elif num1 <= num2:
        print(f"{num1} is less than or equal to {num2}")
    elif num1 > num2:
        print(f"{num1} is greater than {num2}")
    elif num1 >= num2:
        print(f"{num1} is greater than or equal to {num2}")
    elif num1 == num2:
        print(f"{num1} and {num2} are equal")
    else:
        print("Invalid number")

# Example usage
num1 = 5
num2 = 10
compare_numbers(num1, num2)

num1 = 10
num2 = 10
compare_numbers(num1, num2)

num1 = 15
num2 = 10
compare_numbers(num1, num2)
