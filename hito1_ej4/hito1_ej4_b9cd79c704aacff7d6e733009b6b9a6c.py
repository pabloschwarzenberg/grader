#Conversión de Decimal a Binario
num_deci = int(input("Ingrese número: "))
list_1 = []
while num_deci>0:
  resto = int(num_deci%2)
  list_1.append(resto)
  num_deci = (num_deci-resto)/2
nume_bin = ""
for e in list_1[::-1]:
  nume_bin = nume_bin + str(e)
print("resultado="+str(nume_bin))