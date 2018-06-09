# 1. Loops
"""
1. for
2. while

"""

# For Loop
price_list = []
# range(0,100,1)
# Initialization : 0 is like i=0
# Condition : 100 is like i<100
# Incrementation : 1 is like i++
for i in range(0,100,1):
    price_list = price_list + [i]

print(price_list)


price_list = []
for i in range(0,100,2):
    price_list = price_list + [i]
    #[]+[0] = [0]
    #[0]+[1] = [0,1]
    # [0,1]+[2] = [0,1,2]
print(price_list)

#i=0,i<100,i++


# While Loop
price_list = []
# Initialization : 0 is like i=0
i=0
print("While Loop")
# Condition : 100 is like i<100
while(i<100):
    price_list = price_list + [i]
    # Incrementation : 1 is like i++
    i = i + 1
print(price_list)


# Break in loop

price_list = []
# Initialization : 0 is like i=0
i=0
print("Break Loop")
# Condition : 100 is like i<100
while(i<100):
    price_list = price_list + [i]
    # Incrementation : 1 is like i++
    i = i + 1
    if (i==50):
        print("Break")
        break

print(price_list)

# Continue in Loop

price_list = []
# Initialization : 0 is like i=0
i=0
print("Continue Loop")
# Condition : 100 is like i<100
while(i<100):
    price_list = price_list + [i]
    # Incrementation : 1 is like i++
    i = i + 1
    if (i==50):
        print("Continue")
        pass

print(price_list)

print("Pass")
# Pass in loop
for i in range(0,100):
    pass


print("Continue")
# Pass in loop
for j in range(0,50):
    for i in range(0,100):
        break
    print(j)