#Factores Primos
numero = int(input("Ingrese un número entero: "))
dos = ""
tres = ""
cinco = ""
siete = ""
once = ""
trece = ""
while numero != 1:
 if numero % 2 == 0:
  numero = numero // 2
  dos = dos + "2\n"
 if numero % 3 == 0:
  numero = numero // 3
  tres = tres + "3\n"
 if numero % 5 == 0:
  numero = numero // 5
  cinco = cinco + "5\n"
 if numero % 7 == 0:
  numero = numero // 7
  siete = siete + "7\n"
 if numero % 11 == 0:
  numero = numero // 11
  once = once + "11\n"
 if numero % 13 == 0:
  numero = numero // 13
  trece = trece + "13\n"
else:
 print(dos,tres,cinco,siete,once,trece,sep="")