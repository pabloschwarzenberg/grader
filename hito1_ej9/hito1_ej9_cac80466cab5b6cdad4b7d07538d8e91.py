#Sistema de Ecuaciones
x1=int(input("Ingrese el valor de x en la primera ec: "))
y1=int(input("Ingrese el valor de y en la primera ec: "))
c1=int(input("Ingrese el valor de c en la primera ec: "))
#EC 2
x2=int(input("Ingrese el valor de x en la segunda ec: "))
y2=int(input("Ingrese el valor de y en la segunda ec: "))
c2=int(input("Ingrese el valor de c en la segunda ec: "))
for x in range(-25,15):
    rx=round((c1-(x1*x))/y1,1)
    xd=round(x1*x+y1*rx,1)
    xdd=round(x2*x+y2*rx,1)
    if xd==c1 and xdd==c2:
        a=float(x)
        print("x=",a)
        print("y=",rx)