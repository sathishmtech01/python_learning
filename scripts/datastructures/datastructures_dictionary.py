# dictionary {"key":value} - pairs "json kind"

# information of profile
information = {"name":"csk",
               "age":27,
               "city":"bangalore",
               "area":"btm"}

print(information)
# accessing the value of dictionary
print(information["name"])
print(information["age"])
print(information["city"])
print(information["area"])

# function in dicionary
print(dir(information))

# Assignment :
# ['clear', 'copy', 'fromkeys', 'get',
# 'items', 'keys', 'pop', 'popitem',
# 'setdefault', 'update', 'values']

print(information.items())
print(information.keys())
print(information.values())

for key,value in information.items():
    print(key,value)