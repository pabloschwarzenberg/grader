#Cálculo del dígito verificador de un rut
R=int(input())
n1=int(R//(10000000))
segundo_digito=int(R//(1000000)%10)
tercer_digito=int(R//(100000)%10)
cuarto_digito=int(R//(10000)%10)
quinto_digito=int(R//(1000)%10)
sexto_digito=int(R//(100)%10)
septimo_digito=int(R//(10)%10)
octavo_digito=int(R//(1)%10)
a=int((octavo_digito)*2)
b=int((septimo_digito)*3)
c=int((sexto_digito)*4)
d=int((quinto_digito)*5)
e=int((cuarto_digito)*6)
f=int((tercer_digito)*7)
g=int((segundo_digito)*2)
h=int((n1)*3)
suma=(a+b+c+d+e+f+g+h)
resto=suma%11
digito=11-resto
if digito==11:
  print("dv=0")
elif digito==10:
  print("dv=k")
else: 
  print("dv=",digito)