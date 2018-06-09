
# Functions Learning
"""

1. Functions with return value
"""

# Functions with return

# single return - specific data type format
def add(a,b):
    """

    :param a:
    :param b:
    :return:
    """

    c= a+b
    return c

# multiple return - tuple format
def multiple_return(a,b):
    """

    :param a:
    :param b:
    :return:
    """

    return a,b

# Default Parameters with arguments
def add_withdefaults(a=10,b=30):
    """

    :param a:
    :param b:
    :return:
    """
    c= a+b

    return c

# Default Parameters with arguments  and no return statement
def add_without_return(a=10,b=30):
    """

    :param a:
    :param b:
    :return:
    """
    c= a+b

    #return c


# Ananymous function
anaymous_fn = lambda x : x+1

#Or
# Normal function with the above anoynmous functionality
def anaymous_fn1(x):
    return x+1

# Main function - Initiation of the functions execution at first
# similar to public static void main in java
if __name__ == '__main__':
    a=10
    b=20

    # single return
    d =add(10, 20)
    print(d)

    # multiple return - tuple format
    c= multiple_return(a,b)
    print(c)
    print(type(c))


    # Passing arguments directly
    print(add(a=10,b=40))

    # passing arrguments with default
    print(add_withdefaults())

    # without return
    print(add_without_return())

    # ananymous function call
    print(anaymous_fn(10))

    # similar to ananymous with normal function
    print(anaymous_fn1(10))