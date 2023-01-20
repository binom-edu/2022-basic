def faktorial(n):
    if n == 1:
        return 1
    return faktorial(n - 1) * n

def fib(n):
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

print(faktorial(5))
print(fib(7))