#Sistema de Ecuaciones
a=float(input())
b=float(input())
c=float(input())
d=float(input())
e=float(input())
f=float(input())
b1=(b*d)
c1=(c*d)
e1=(e*a*-1)
f1=(f*a*-1)
y=(c1+f1)/(b1+e1)
x=(c-y)/a
frase="['x="+str(x)+"', 'y="+str(y)+"']"
print(frase)