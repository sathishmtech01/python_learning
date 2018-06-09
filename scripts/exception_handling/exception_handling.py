# 1. Exception Handling
"""
1. try
2. except
3. finally
"""

# Simple try-except block
personal_details = {"name":"csk","age":25}

# Error - KeyError
#print(personal_details["city"])

try:
    print(personal_details["city"])

except(KeyError,AttributeError) as err:
    personal_details["city"] = "Bangalore"
    print("Exception Block")
    print(personal_details["city"])
except:
    pass

# try-except-finally block

print("try-except-finally block")
try:
    print(personal_details["city"])

except(KeyError):
    personal_details["city"] = "Bangalore"
    print("Exception Block")
    print(personal_details["city"])
finally:
    print("Finally")