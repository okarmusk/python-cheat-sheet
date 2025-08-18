# Dictionaries
phone_book = {'k': 1234, 'o': 1235}
phone_book['m'] = 1233
phone_book['b'] = 1236
phone_book['k'] = 1237
del phone_book['o']
print(phone_book)
print(list(phone_book))
print(sorted(phone_book))

if 'o' not in phone_book:
    phone_book['o'] = 1238

print(phone_book)

# Looping
for k, v in phone_book.items():
    print(k, v)

keys = ['k0', 'k1', 'k3']
values = ['v0', 'v1', 'v2']

for k, v in zip(keys, values):
    print(k, v)

# Comparing sequences
# (1, 2, 3)              < (1, 2, 4)
# [1, 2, 3]              < [1, 2, 4]
# 'ABC' < 'C' < 'Pascal' < 'Python'
# (1, 2, 3, 4)           < (1, 2, 4)
# (1, 2)                 < (1, 2, -1)
# (1, 2, 3)             == (1.0, 2.0, 3.0)
# (1, 2, ('aa', 'ab'))   < (1, 2, ('abc', 'a'), 4)

if (1, 2, 3, 4) < (1, 2, 4):
    print(True)
