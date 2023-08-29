#Cálculo del dígito verificador de un ru

rut = int(input("Ingrese su rut: "))

a=(rut//10000000) * 3
b=((rut//1000000)%10) * 2
c=((rut//100000)%10) * 7
d=((rut//10000)%10) * 6
e=((rut//1000)%10) * 5
f=((rut//100)%10) * 4
g=((rut//10)%10) * 3
h=((rut//1)%10) * 2

sumatotal=(a+b+c+d+e+f+g+h)
resto= sumatotal // 11
resto2= sumatotal-(11*resto)
resta=11-resto2

if (resta == 11):
  print("dv=",end="")
  print(0)

elif (resta == 10):
  print("dv=",end="")
  print("k")

else:
  print("dv=",end="")
  print(resta)