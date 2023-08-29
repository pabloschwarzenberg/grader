#Conversión de Decimal a Binario
a = int(input("Escribe un numero:"))
list = []
while (a > 0):
  c = int(a%2)
  list.append(c)
  a = (a - c)/2
a_bin = ""
for b in list[::-1]:
 a_bin = a_bin + str(b)
print("resultado ="+str(a_bin))
      