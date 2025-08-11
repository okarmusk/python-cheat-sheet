import re

short_string = 'short sting'
long_string = '''

very, very long string

'''
string_with_backslash = ('string with \ '
                         'backslash') # same rule is applied to ''' quote stings

# String literal concatenation
re.compile("[A-Za-z]"
           "[A-Za-z0-9_]*")

# f-strings
name = 'Konrad'
f_string = f"Welcome in real world {name}."
f_string_with_operation = f"Operation result: {8^2}"

arr = ['a', 'b', 'c']
f_string_join = f"{"\n".join(arr)}"

# Numeric literals
# Integer literals:
# 7     2147483647                        0o177    0b100110111
# 3     79228162514264337593543950336     0o377    0xdeadbeef
#       100_000_000_000                   0b_1110_0101

# Floating point literals
# 3.14    10.    .001    1e100    3.14e-10    0e0    3.14_15_93

# Imaginary literals
# 3.14j   10.j    10j     .001j   1e100j   3.14e-10j   3.14_15_93j
