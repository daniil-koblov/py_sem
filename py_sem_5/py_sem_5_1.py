def fib(n):
    if n in [0, 1]: return 1
    return fib(n - 1) + fib(n - 2)

n = int(input('Введите число: '))

print(fib(n - 2))