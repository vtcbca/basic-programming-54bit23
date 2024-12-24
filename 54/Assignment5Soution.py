def is_palindrome_recursive(input_string):
    if len(input_string) <= 1:
        return True
    if input_string[0] != input_string[-1]:
        return False
    return is_palindrome_recursive(input_string[1:-1])

# Example usage
input_string = "madam"
print(is_palindrome_recursive(input_string))  # Output: True
