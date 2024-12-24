def print_triangle(n, current=1):
    if current > n:
        return
    print(" " * (n - current) * 2 + " ".join(str(i) for i in range(1, 2 * current)))
    print_triangle(n, current + 1)

n = int(input("Enter the number of lines: "))
print_triangle(n)
