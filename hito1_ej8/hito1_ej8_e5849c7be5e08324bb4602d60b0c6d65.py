numero = input("Ingrese un numero de maximo 4 digitos: ")
longitud = len(numero)
Mil = "M"
Centena = "C"
Decena = "D"
Unidad = "U"
if longitud == 4:
  r1 = numero[0:1]+Mil
  r2 = numero[1:2]+Centena
  r3 = numero[2:3]+Decena
  r4 = numero[3:4]+Unidad
  print(r1,"+",r2,"+",r3,"+",r4)
if longitud == 3:
  r1 = numero[0:1]+Centena
  r2 = numero[1:2]+Decena
  r3 = numero[2:3]+Unidad
  print(r1,"+",r2,"+",r3)
if longitud == 2:
  r1 = numero[0:1]+Decena
  r2 = numero[1:2]+Unidad
  print(r1,"+",r2)
if longitud ==1:
  r1 = numero[0:1]+Unidad
  print(r1)

