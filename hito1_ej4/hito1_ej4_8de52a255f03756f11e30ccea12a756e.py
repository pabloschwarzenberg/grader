#Conversión de Decimal a Binario
n = int(input("ingrese numero decimal:")) 

lista = []
while n>0:
   resto = int(n%2)
   lista.append(resto)
   n = (n-resto)/2
   
n_bin = ""

for e in lista[: :-1]:
  n_bin = n_bin + str(e)
  print("resultado="+str(n_bin))      