#Cálculo del dígito verificador de un rut

a=int(input("Ingrese el rut: "))
b=(a//10000000)*3
c=((a//1000000)%10)*2
d=((a//100000)%10)*7
e=((a//10000)%10)*6
f=((a//1000)%10)*5
g=((a//100)%10)*4
h=((a//10)%10)*3
i=((a//1)%10)*2
dv=(b+c+d+e+f+g+h+i)
dv1= dv // 11
dv2=dv-(11*dv1)
dv3=11-dv2
if dv3 == 11:
  print("dv=",end="")
  print(0)
if dv3 == 10:
  print("dv=",end="")
  print("k")
else:
  print("dv=",end="")
  print(dv3)