#Convertir un decimal a binario
x=eval(input("Ingrese un decimal: "))
a=int(x)%2
a1=int(x)/2
b=int(a1)%2
b1=int(a1)/2
c=int(b1)%2
c1=int(b1)/2
d=int(c1)%2
d1=int(c1)/2
e=int(d1)%2
e1=int(d1)/2
f=int(e1)%2
f1=int(e1)/2
g=int(f1)%2
g1=int(f1)/2
h=int(g1)%2
h1=int(g1)/2
a2=str(a)
b2=str(b)
c2=str(c)
d2=str(d)
e2=str(e)
f2=str(f)
g2=str(g)
h2=str(h)
y=h2+g2+f2+e2+d2+c2+b2+a2
print("resultado={}".format(int(y)))
