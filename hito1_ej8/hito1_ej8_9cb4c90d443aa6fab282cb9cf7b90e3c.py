#Descomponer un número
k = "UDCM"
largo = 5
while (largo > 4):
  num = input("Ingrese un numero de hasta 4 dígitos -> ")
  largo = len(num)
final = ""
for i in range(len(num)):
  final = num[len(num)-1-i] + k[i] + final
  if(i < len(num)-1):
    final = " + " + final
print(final)