# Set operation
# TODO: Note : myself: In set duplicates are removed
set_A = {1,2,3,4,10,21,21,21}
set_B = {10,4,3,2,1}

# And or intersection operation
print(set_A & set_B)

# Or or Union operation
print(set_A | set_B)

#
print(dir(set_A))

# Assignments : ['add', 'clear', 'copy',
# 'difference', 'difference_update',
# 'discard', 'intersection',
# 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove',
#  'symmetric_difference',
# 'symmetric_difference_update', 'union',
# 'update']

set_A.add(100)
print(set_A)
# pop remove the first element
set_A.pop()
# reove, needs to specify the element
set_A.remove(2)
#set_A - set_B
print(set_A.difference(set_B))