#Cálculo del dígito verificador de un rut
rut=int(input("ingresar rut sin digito verificador: "))
a=rut//10000000
b=(rut//1000000)%10
c=(rut//100000)%10
d=(rut//10000)%10
e=(rut//1000)%10
f=(rut//100)%10
g=(rut//10)%10
h=rut%10
i=h*2
j=g*3
k=f*4
l=e*5
m=d*6
n=c*7
o=b*2
p=a*3
suma=i+j+k+l+m+n+o+p
flash=suma//11
arrow=suma-(11*flash)
batman=11-arrow
if batman==11:
   print("dv=0")
elif batman==10:
   print("dv=k")
else:
   print("dv=",batman)

