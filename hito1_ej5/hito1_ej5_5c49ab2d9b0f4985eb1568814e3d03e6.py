#Cálculo del dígito verificador de un rut
rut=int(input("da el rut"))
x=rut
a=x//(10000000)
x=x%(10000000)
b=x//(1000000)
x=x%(1000000)
c=x//(100000)
x=x%(100000)
d=x//(10000)
x=x%(10000)
e=x//(1000)
x=x%(1000)
f=x//(100)
x=x%(100)
g=x//(10)
x=x%(10)
h=x//(1)
x=x%(1)
w=int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h))
i=int(h)*2
j=int(g)*3
k=int(f)*4
l=int(e)*5
m=int(d)*6
n=int(c)*7
ñ=int(b)*2
o=int(a)*3
la_suma=(i+j+k+l+m+n+ñ+o)
division=(la_suma//11)
z=la_suma-(11*division)
digito_verificador=11-z
if digito_verificador==11:
    digito_verificador=0
elif digito_verificador==10:
    digito_verificador="K"
else:
    digito_verificador=digito_verificador
print("dv="+str(digito_verificador))