# 1! = 1
# 2! = 2 * 1
# 3! = 3 * 2 * 1
# 4! = 4 * 3 *2 *1
# 2 = [1, 2]
# value = 1
# value = value * second item


# Iterative Function
def n_factorial_iteration(n):
    value = 1

    for i in range(1, n + 1):
        value = value * i
    return value

# Recursive Function
def n_factorial_recursion(n):
    if n == 1:
        return 1

    return n * n_factorial_recursion(n-1)


print(n_factorial_regit cursion(7))