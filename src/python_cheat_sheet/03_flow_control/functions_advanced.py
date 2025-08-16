
def function(arg0, *arguments, **keywords):
    for arg in arguments:
        print(arg)
    for key in keywords:
        print(key, ":", keywords[key])

function("Required argument0", "a1", "a2",
         k0 = "keyword0", k1 = "keyword1", k2 = "keyword2")

# Special parameters
# Positional or keyword arguments
# / and * are optional. If used, these symbols indicate the kind of parameter by how the arguments
# may be passed to the function: positional-only, positional-or-keyword, and keyword-only.
# Keyword parameters are also referred to as named parameters.

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

combined_example(1, 2, kwd_only = 3)
combined_example(1, standard = 2, kwd_only = 3)


# Lambda expressions
def power(n):
    return lambda x: n ** x

two_power = power(2)
print(two_power(128))

# Function Annotations
def map_to_str(number) -> str:
    print(map_to_str.__annotations__)
    return str(number)

print(map_to_str(128))
