#Sistema de Ecuaciones
x=0
y=0
a1=int(input("ingresa"))
b1=int(input("ingresa"))
c1=int(input("ingresa"))
a2=int(input("ingresa"))
b2=int(input("ingresa"))
c2=int(input("ingresa"))
if a1==0:
    print("anda a laar")
else:
    y=(c2-((a2*c1)/a1))/(b2-((a2*b1)/a1))
    print("y=",y)
    x=(c1-(b1*y))/a1
    print("x=",x)     