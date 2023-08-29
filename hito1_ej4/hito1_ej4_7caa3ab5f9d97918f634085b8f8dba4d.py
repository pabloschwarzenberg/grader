numero = int(input("Ingrese un numero decimal positivo:"))
binario = ""
if (numero > 0):
  while numero > 0:
    if (numero%2 == 0):
      binario = "0" + binario
else:
  binario = "1" + binario
  numero = int(numero/2)
  print("El resultado de la conversion es: "+binario)



