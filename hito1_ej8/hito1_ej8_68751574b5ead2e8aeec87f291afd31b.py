#Descomponer un número
numero = int(input("ingrese un número de hasta 4 digitos: )
if 0 < numero < 10000:
  miles = numero // 1000
  centena = (numero % 1000) // 100
  decena = ((numero % 1000) % 100) // 10
  unidad = ((numero % 1000) % 100) % 10
  print(miles,"M +", centena, "C +", decena "D +" unidad, U)
else:
   print("Debe ser un número de hasta 4 dígitos.")