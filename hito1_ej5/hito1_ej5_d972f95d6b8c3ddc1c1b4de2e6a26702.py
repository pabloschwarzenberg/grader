#Cálculo del dígito verificador de un rut

r = int(input("Favor de ingresar el rut: "))

a=(r//10000000) * 3
b=((r//1000000)%10) * 2
c=((r//100000)%10) * 7
d=((r//10000)%10) * 6
e=((r//1000)%10) * 5
f=((r//100)%10) * 4
g=((r//10)%10) * 3
h=((r//1)%10) * 2

s = (a+b+c+d+e+f+g+h)
resta = s // 11
resta1 = s - (11*resta)
resta2 = 11 - resta1

if resta2 == 11:
  print("dv=" , end="")
  print(0)
elif resta2 == 10:
  print("dv=" , end="")
  print("k")
else:
  print("dv=" , end="")
  print(resta2)
  