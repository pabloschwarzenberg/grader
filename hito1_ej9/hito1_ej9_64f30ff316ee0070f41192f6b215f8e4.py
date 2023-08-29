a=int(input("Ingresa a: "))
b=int(input("Ingresa b: "))
c=int(input("Ingresa c: "))
d=int(input("Ingresa d: "))
e=int(input("Ingresa e: "))
f=int(input("Ingresa f: "))
Determinante=a*e-b*d

if Determinante==0:
   Print('no tiene solucion')
else:
   x=float((c*e)-(b*f))
   x=float(x/Determinante)
   y=float((a*f)-(c*d))
   y=float(y/Determinante)

print('x=',x)
print('y=',y)

      