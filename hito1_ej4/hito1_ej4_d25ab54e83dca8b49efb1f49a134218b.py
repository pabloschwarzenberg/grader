x = int(input("Ingrese su número  decimal: ")) 

lista = [] 

while x>0: 

  resto = int(x%2) 

  lista.append(resto) 

  x = (x-resto)/2 

x_bin = "" 

for e in lista[::-1]: 

  x_bin = x_bin + str(e) 

print("resultado="+str(x_bin))