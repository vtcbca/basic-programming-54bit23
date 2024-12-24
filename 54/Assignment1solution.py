def factorial_using_while_loop(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Example usage
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial_using_while_loop(number)}")
