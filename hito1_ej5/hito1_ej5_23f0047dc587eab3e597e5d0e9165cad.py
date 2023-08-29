#Cálculo del dígito verificador de un rut
rut=int(input())
#digitos
n1=int(rut//(10000000))
n2=int(rut//(1000000)%10)
n3=int(rut//(100000)%10)
n4=int(rut//(10000)%10)
n5=int(rut//(1000)%10)
n6=int(rut//(100)%10)
n7=int(rut//(10)%10)
n8=int(rut//(1)%10)

a=n8*2
b=n7*3
c=n6*4
d=n5*5
e=n4*6
f=n3*7
g=n2*2
h=n1*3

suma=(a+b+c+d+e+f+g+h)
modulo=(suma%11)
digito=(11-modulo)

if digito==11:
  print("dv=0")
elif digito==10:
  print("dv=k")
else:
  print("dv=",digito)