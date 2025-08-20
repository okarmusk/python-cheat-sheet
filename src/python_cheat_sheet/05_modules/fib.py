def fibonacci(n: int) -> list:
    fib = []
    a, b = 0, 1
    while a < n:
        fib.append(a)
        a, b = b, a + b
    return fib
