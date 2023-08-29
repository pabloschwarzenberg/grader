#Conversión de Decimal a Binario
numero = int(input("Ingrese número: "))

lista = []

while numero>0:

  resto = int(numero%2)

  lista.append(resto)

  numero = (numero-resto)/2

numero_bin = ""

for e in lista[::-1]:

  numero_bin = numero_bin + str(e)

print("resultado="+str(numero_bin))      