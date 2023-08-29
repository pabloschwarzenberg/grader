#Conversión de Decimal a Binario
Number = int(input("adjunte un número decimal: ")) 

lista = [] 

while Number>0: 

  resto = int(Number%2) 

  lista.append(resto) 

  Number = (Number-resto)/2 

Number_bin = "" 

for e in lista[::-1]: 

  Number_bin = Number_bin + str(e) 

print("resultado="+str(Number_bin))
