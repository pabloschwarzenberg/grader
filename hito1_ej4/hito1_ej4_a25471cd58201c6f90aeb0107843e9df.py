#Conversión de Decimal a Binario
num = int(input("ingrese numero decimal:"))
registro = []
while num>0:
   resto = int(num%2)
   registro.append(resto)
   num = (num-resto)/2
num_bin = ""
for e in registro[: :-1]:
  num_bin = num_bin + str(e)
  print("resultado="+str(num_bin))      