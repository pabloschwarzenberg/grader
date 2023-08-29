#Cálculo del dígito verificador de un rut
numero_rut=int(input("Ingrese el rut: "))
a=(numero_rut//10000000) * 3

b=((numero_rut//1000000)%10) * 2

c=((numero_rut//100000)%10) * 7

d=((numero_rut//10000)%10) * 6

e=((numero_rut//1000)%10) * 5

f=((numero_rut//100)%10) * 4

g=((numero_rut//10)%10) * 3

h=((numero_rut//1)%10) * 2

suma=(a+b+c+d+e+f+g+h)

resto1= suma // 11

resto2=suma-(11*resto1)

menos=11-resto2
if menos == 11:
  print("dv=",end="")
  print(0)
elif menos == 10:
   print("dv=",end="")
   print("k")
else:
  print("dv=",end="")
  print(menos)