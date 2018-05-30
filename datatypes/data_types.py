# data types
# Single line comment
"""
Multi line comment
"""
# variable declarations

# String variable declations
name_with_doubequotes ="'csk'"
name_with_siglequote = '"csk"'
# TODO : Need to explore
# it is for multi line parsing
name_with_triplequote = """
csk
csk
"""

print(name_with_doubequotes)
print(name_with_siglequote)
print(name_with_triplequote)

# checking the type of the variable
print(type(name_with_doubequotes))
# Output: <class 'str'>

# work around the variable - possibile functions
print(dir(name_with_siglequote))
# Output ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
print(name_with_siglequote.upper())


# variable declaration integer

age = 26
print(age)
print(type(age))
print(dir(age))

# Getting the function
print(help(str.zfill))

# same applicable for float


