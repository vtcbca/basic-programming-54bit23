def print_alphabet_pattern(n, current=1):
    if current > n:
        return
    spaces = " " * (n - current) * 2
    first_half = [chr(64 + j) for j in range(1, current + 1)]
    second_half = [chr(64 + j) for j in range(current - 1, 0, -1)]
    print(spaces + " ".join(first_half + second_half))
    print_alphabet_pattern(n, current + 1)

n = int(input("Enter the number of lines: "))
print_alphabet_pattern(n)
