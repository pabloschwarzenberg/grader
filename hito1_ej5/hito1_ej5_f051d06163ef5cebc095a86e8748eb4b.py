#Cálculo del dígito verificador de un rut
r= int(input("ingrese dato: "))
mod=11
a=r%10
b1=r%100
b=b1//10
c1=r%1000
c=c1//100
d1=r%10000
d=d1//1000
e1=r%100000
e=e1//10000
f1=r%1000000
f=f1//100000
g1=r%10000000
g=g1//1000000
h=r//10000000
n1=a*2
n2=b*3
n3=c*4
n4=d*5
n5=e*6
n6=f*7
n7=g*2
n8=h*3
suma=n1+n2+n3+n4+n5+n6+n7+n8
a2=suma//mod
a3=suma-(mod*a2)
dv=mod-a3
if dv==11:
    print("dv=0")
elif dv==10:
    print("dv=k")
else:
    print ("dv=",(dv))