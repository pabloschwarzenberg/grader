x =int(input("1: "))
y =int(input("2: "))
z =int(input("3: "))
a= min(x,y,z)
c= max(x,y,z)
b= (x+y+z)-a-c
print("{},{},{}".format(a,b,c))