#Conversión de Decimal a Binario
num = int(input("ingrese el numero decimal: "))
datos = []
string = ""
while num>0:
  binari = num%2
  num = num//2
  datos.append(binari)
contador = 0
datos.reverse()
while contador<len(datos):
  string = string + str(datos[contador])
  contador = contador+1

print("resultado=",string)
  