numero = int(input("Ingrese número decimal para asi pasarlo a binario: "))
lista = []
while numero > 0:
  resto = int(numero %2)
  lista.append(resto)
  numero = (numero - resto)/2
binario = ""
for e in lista[::-1]:
  binario = binario + str(e)
print("resultado="+str(binario))