print("ax+by=c")
print("dx+ey=f")
a=float(input("Valor de a: "))
b=float(input("Valor de b: "))
c=float(input("Valor de c: "))
d=float(input("Valor de d: "))
e=float(input("Valor de e: "))
f=float(input("Valor de f: "))
g=d*b-a*e
if g==0:
    print("No se puede resolver")
else:
    x=(f*b-c*e)/(d*b-a*e)
    print("x=",x)
    y=(c-a*x)/b
    print("y=",y)