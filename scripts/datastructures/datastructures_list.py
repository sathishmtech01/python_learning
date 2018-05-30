# array|list
#element list of array with same data types
element_list = ["apple","orange","grapes"]
# element list of array with different data types
element_list_mutiple_dt = ["apple","orange","grapes",12,2.5]

# index starts from zero

print(element_list[0])
print(element_list_mutiple_dt)

# numeric list
age_list = [21,22,23,24,25]
print(age_list)

# for loop in one line
# list comprehension
age_list_10 = [i+10 for i in age_list]
print(age_list_10)
print(dir(age_list_10))

# Assignment : Explore array|list functions
# ['append', 'clear', 'copy', 'count',
# 'extend', 'index', 'insert', 'pop', 'remove',
# 'reverse', 'sort']

age_list_10.append(20)
print(age_list_10)

