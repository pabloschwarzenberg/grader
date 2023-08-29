#Conversión de Decimal a Binario
n = int(input("Ingrese número decimal: ")) 
lista = [] 
while n>0: 
  resto = int(n%2) 
  lista.append(resto) 
  n = (n-resto)/2 
n_bin = "" 
for e in lista[::-1]: 
  n_bin = n_bin + str(e) 
print(n_bin)