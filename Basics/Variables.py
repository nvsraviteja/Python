x = 10

def my_function():
    global x
    x = 20
    print("Local variable:", x)


my_function()

print("Global variable:", x)