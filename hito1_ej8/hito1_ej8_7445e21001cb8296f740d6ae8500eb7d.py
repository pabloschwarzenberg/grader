#descomposocion
numero = int(input("ingrese un numero de 4 digitos para descomponerlo "))
m=0
c=0
d=0
u=0
if numero > 9999:
  print("ingrese un numero de 4 digitos ")
elif numero > 999 and numero <= 9999:
  numero = str(numero)
  m = numero[0]
  c = numero[1]
  d = numero[2]
  u = numero[3]
  print(m,"M +",c,"C +",d,"D +",u,"U")
elif numero > 99 and numero <= 999:
  numero = str(numero)
  c = numero[0]
  d = numero[1]
  u = numero[2]
  print(c,"C + ",d,"D +",u,"U")
elif numero > 9 and numero <= 99:
  numero = str(numero)
  d = numero[0]
  u = numero[1]
  print(d,"D +", u,"U")
elif numero >= 1 and numero <= 9:
  numero = str(numero)
  u = numero
  print(u,"U")