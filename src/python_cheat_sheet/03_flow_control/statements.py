# If statement
x = 128

if x > 64:
    print("x > 64")
elif x == 128:
    print("x == 128")
else:
    print("Unexpected value")

# For statement
letters = ['a', 'b', 'c', 'd', 'e']

for l in letters:
    print(l, end = ',')

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    if i == 8:
        break

# Else in loops
# 'else' in loops is NOT executed if loop was terminated by 'break'

for i in range(2):
    if i == 3:
        break
else:
    print("Achieved for else block.")

# Pass
# 'pass' statement does nothing, it is used when statement is required syntactically, but program requires no action
def do_nothing():
    pass # Just do nothing

# Match
def try_match(letter):
    match letter:
        case 'a':
            return 'A'
        case 'b':
            return 'B'
        case 'c':
            return 'C'
        case _:
            raise ValueError('Unknown letter')
