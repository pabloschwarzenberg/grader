#Conversión de Decimal a Binario


numero = float(input("Ingrese número decimal: "))
lista = []
while numero>0:

 n1 = int(numero % 2)

 lista.append(n1)

 numero = (numero - n1)/2

numero_bin = ""

for i in lista[::-1]:

  numero_bin = numero_bin + str(i)

print("resultado="+ str(numero_bin)) 
