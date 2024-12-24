def print_pattern_concatenation(n):
    for i in range(1, n + 1):
        row = ''
        for j in range(i):
            row += '* '
        print(row.strip())

# Example usage
n = 4
print_pattern_concatenation(n)
