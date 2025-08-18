# Sets
python = {'p', 'y', 't', 'h', 'o', 'n', 'n'}
print(python)

if 'p' in python:
    print('p is present')

# Operations on sets
thon = {'t', 'h', 'o', 'n'}
py = python - thon
print(py)
diff_set = thon - python
print(diff_set) # Empty set
or_set = python | thon
print(or_set)
and_set = python & thon
print(and_set)
nor_set = python ^ thon
print(nor_set)
