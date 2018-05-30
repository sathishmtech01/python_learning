price = 0

# Normal conditional flow
if price>50 and  price <100:
    print("price if : ",price)
elif price<50 and price >1 :
    print("price elif : ",price)
else:
    print("price else : ", price)


price = 31
# conditional flow in array
if price in [1,12,3]:
    print("price if : ",price)
elif price in [21,31,41] :
    print("price elif : ",price)
else:
    print("price else : ", price)