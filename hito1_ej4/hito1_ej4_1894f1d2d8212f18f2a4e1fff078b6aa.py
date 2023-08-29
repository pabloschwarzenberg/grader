#Conversión de Decimal a Binario
num = int(input("ingrese numero decimal:"))
lista = []
while num>0:
   resto = int(num%2)
   lista.append(resto)
   num = (num-resto)/2
num_bin = ""
for e in lista[: :-1]:
  num_bin = num_bin + str(e)
  print("resultado="+str(num_bin))