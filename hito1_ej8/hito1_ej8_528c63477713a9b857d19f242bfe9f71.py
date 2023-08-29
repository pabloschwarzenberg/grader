y = int(input("1"))
y = str(y)
x = len(y)
if x == 4:
    a = y[0]
    b = y[1]
    c = y[2]
    d = y[3]
    print(a,"M+",b,"C+",c,"D+",d,"U")
elif x == 3:
    a = y[0]
    b = y[1]
    c = y[2]
    print(a, "C+", b, "D+", c, "U")
elif x == 2:
    a = y[0]
    b = y[1]
    print(a, "D+", b, "U")
elif x == 1:
    a = y[0]
    print( a, "U")
