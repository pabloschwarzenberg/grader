#Rut
rut=int(input("Ingrese su Rut: "))
d1F=rut//10000000
d1F=int(d1F)
d2O=rut//1000000
d2O=int(d2O)
d2F=d2O%10
d3O=rut//100000
d3O=int(d3O)
d3F=d3O%10
d4O=rut//10000
d4O=int(d4O)
d4F=d4O%10
d5O=rut//1000
d5O=int(d5O)
d5F=d5O%10
d6O=rut//100
d6O=int(d6O)
d6F=d6O%10
d7O=rut//10
d7O=int(d7O)
d7F=d7O%10
d8F=rut%10
d8F=int(d8F)
#Ecuacion
a=d8F*2
a=int(a)
b=d7F*3
b=int(b)
c=d6F*4
c=int(c)
d=d5F*5
d=int(d)
e=d4F*6
e=int(e)
f=d3F*7
f=int(f)
g=d2F*2
g=int(g)
h=d1F*3
h=int(h)
Suma=a+b+c+d+e+f+g+h
Suma=float(Suma)
factor_a=Suma//11
factor_a=float(factor_a)
factor_b=Suma-(11*factor_a)
factor_b=float(factor_b)
final=11-factor_b
final=float(final)
if final==10 :
    print("dv=K")

if final==11 :
    print("dv=0")
if final<=9 :
    print("dv=",int(final))