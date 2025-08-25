def generator():
    for i in range(10):
        yield i

for g in generator():
    print(g)
