# More on lists
print("### More on lists ###")
lst = [1, 2]
lst.append('3')
lst.insert(0, '0')
print(lst)
lst.remove('3')
lst.append(3)
v0 = lst.pop(3)
print(v0, lst)
lst.extend([3, 4, 5, 6, 7 , 8])
print(lst)

# List comprehensions
print("### List comprehensions ###")
sqr = [x ** 2 for x in range(16)]
print(sqr)

lst2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
unpacked_lst = [x for n in lst2d for x in n]
print(unpacked_lst)

elems = [7, 8, 9]
unique_tuple_comb = [(x, y) for x in elems for y in elems if x != y]
print(unique_tuple_comb)

# Del statement
print("### del statement ###")
lst = [0, 1, 2, 3, 4, 5, 6 ,7 ,8]
del lst[0]
print(lst)
del lst[1:3]
print(lst)
del lst[:]
print(lst)
