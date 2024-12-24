def reverse_string_loop(input_string):
    reversed_string = ""
    for char in input_string:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage
input_string = "Hello, World!"
print(reverse_string_loop(input_string))
