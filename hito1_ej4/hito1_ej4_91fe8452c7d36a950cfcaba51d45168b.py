#Conversión de Decimal a Binario
numero=int(input("adjunte un número decimal: ")) 
lista=[] 
while numero>0: 
  resto=int(numero%2) 
  lista.append(resto) 
  numero=(numero-resto)/2 
binario="" 
for e in lista[::-1]: 
  binario=binario+str(e) 
print("resultado="+str(binario))