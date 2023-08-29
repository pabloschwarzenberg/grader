numero = int(input("decimal: "))
lista = []
while numero>0:
  resto = int  (numero%2)
  lista.append(resto)
  numero = (numero-resto)/2
numero_binario = ""
for e in lista[::-1]:
  numero_binario = numero_binario + str(e)
print("resultado="+str(numero_binario))