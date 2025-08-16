# Basic function definition
def fib(n):
    """Returns list containing Fibonacci series up to n"""
    f_seq = []
    a, b = 0, 1

    while a < n:
        f_seq.append(a)
        a, b = b, a + b
    print(f_seq)

    return f_seq

fib(128)

# Default function arguments
def fib_with_def(n = 256):
    """Returns list containing Fibonacci series up to n, where n by default equals 256"""
    f_seq = []
    a, b = 0, 1

    while a < n:
        f_seq.append(a)
        a, b = b, a + b
    print(f_seq)

    return f_seq

# Default arguments with evaluation
i = 5

def f(arg=i):
    print(arg)

i = 6
f() # Will print 5

#  The default value is evaluated only once.
#  This makes a difference when the default is a mutable object such as a list,
#  dictionary, or instances of most classes.

def f(a, l = []):
    l.append(a)
    return l

print(f(1))
print(f(2))
print(f(3))

# Will print:
# [1]
# [1, 2]
# [1, 2, 3]

# If you don’t want the default to be shared between subsequent calls, you can write the function like this instead:
def f(a, l = None):
    if l is None:
        l = []
    l.append(a)
    return l

