#Descomponer un número
numero = int(input("Ingrese un numero de hasta 3 dígitos: "))

serie = "UDCM"
descomposicion = ""

posicionSerie = 0

while (numero > 0):
  elemento = str(numero % 10) + serie[posicionSerie]
  posicionSerie = posicionSerie + 1
  numero = numero // 10
  if (numero > 0):
    elemento = " + " + elemento
  descomposicion = elemento + descomposicion

print(descomposicion)