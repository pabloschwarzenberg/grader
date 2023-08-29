#Conversión de Decimal a Binario
numero = int(input("Ingrese número decimal: "))
lista = []
while numero>0:
    resto = int(numero%2)
    lista.append(resto)
    numero = (numero-resto)/2
    nr_bin = ""
for e in lista[::-1]:
    nr_bin = nr_bin + str(e)

print("resultado="+str(nr_bin))