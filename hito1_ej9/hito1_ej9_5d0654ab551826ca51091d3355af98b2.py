#Sistema de Ecuaciones
print("Resolviendo:")
print("ax+by=c")
print("dx+ey=f")

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
d=float(input("d="))
e=float(input("e="))
f=float(input("f="))
if a==0:
    if e==0:
        print("x=",(f/d))
        print("y=",(c/b))
    else:
        y=(c/b)
        x=((f-(e*y))/d)
        print("x=", x)
        print("y=", y)
elif d==0:
    if b==0:
        print("x=",(c/a))
        print("y=",(f/e))
    else:
        y=(f/e)
        x=((c-(b*y))/a)
        print("x=",x)
        print("y=",y)
elif b==0:
    x=(c/a)
    y=((f-(d*x))/e)
    print("x=",x)
    print("y=",y)
elif e==0:
    x=(f/d)
    y=((c-(a*x))/b)
    print("x=",x)
    print("y=",y)
elif (-a/b)==(-d/e) and (c/b)==(f/e):
    print("Tiene infinitas soluciones")
elif (-a/b)==(-d/e):
    print("No tiene solucion")
else:
    y=((f*a)-(d*c))/((a*e)-(d*b))
    x=(c-(b*y))/a
    print("x=",x)
    print("y=",y)  