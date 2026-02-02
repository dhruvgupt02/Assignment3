def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)

number=int(input("Enter the number: "))
print(f"Factorial of {number} is {factorial(number)}")