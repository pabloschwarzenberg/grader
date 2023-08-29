#Sistema de Ecuaciones
u1=float(input("u1 = "))
v1=float(input("v1 = "))
w1=float(input("w1 = "))
u2=float(input("u2 = "))
v2=float(input("v2 = "))
w2=float(input("w2 = "))

if u1/u2 == v1/v2 and v1/v2 == w1/w2:
    print("Hay infinitas soluciones!")
elif u1/u2 == v1/v2 and v1/v2 == w1/w2:
    print("No tiene solución")

else:
    x=(w1*v2-w2*v1)/(u1*v2-u2*v1)
    y=(u1*w2-u2*w1)/(u1*v2-u2*v1)

    print("x=",round(x,1))
    print("y=",round(y,1))      