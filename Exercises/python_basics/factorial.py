try:
    n = int(input("Enter a number: "))
except ValueError:
    print("Please enter a valid integer.")
else:
    if n < 0:
        print("Please enter a non-negative integer.")
    else:
        factorial = 1
        for i in range(1, n+1):
            factorial *= i
        print(f"The factorial of {n} is {factorial}")