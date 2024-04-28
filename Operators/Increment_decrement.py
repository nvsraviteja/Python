def increment(num):
    return num + 1

def decrement(num):
    return num - 1

# Example usage
num = int(input('enter value:'))
print("Original number:", num)

num = increment(num)
print("After increment:", num)

num = decrement(num)
print("After decrement:", num)