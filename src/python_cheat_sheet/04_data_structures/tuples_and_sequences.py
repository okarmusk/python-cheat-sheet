# Tuple declaration
t0 = 1, 2, 3
print(t0)

# Nested tuples
t1 = '1', t0
t2 = ('1', t0) # does exactly the same what declaration in previous line
print(t1)

# Unpack tuple
x, y, z = t0
# a, b = t0 - won't work, too many values to unpack

# Singleton tuple
singleton = '1', # add comma to create single element tuple
print(singleton)
