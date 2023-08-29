#Conversión de Decimal a Binario
 
numero = int(input("Ingrese número decimal: "))
conjunto = []
while numero>0:
  sobra = int(numero%2)
  conjunto.append(sobra)
  numero = (numero-sobra)/2
numero_bin = ""
for e in conjunto[::-1]:
  numero_bin = numero_bin + str(e)
print("resultado="+str(numero_bin))