#Sistema de Ecuaciones

x1 = float(input("n1: "))
y1 = float(input("n2: "))
c1 = float(input("n3: "))

x2 = float(input("n4: "))
y2 = float(input("n5: "))
c2 = float(input("n6: "))

d = x1*y2 - y1*x2

if d != 0:
    x = (c1*y2 - y1*c2)
    y = (x1*c2 - c1*x2)

    print("x="+ str(x),"y="+str(y))

else:
    print("no tiene solcion")    