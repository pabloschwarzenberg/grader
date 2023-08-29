#Descomponer un número
import sys
numero=int(input("Introduzca un número: "))
if numero>9999:
  sys.exit
else:
  miles=int(numero/1000)
  centenas=int((numero-miles*1000)/100)
  decenas=int((numero-miles*1000-centenas*100)/10)
  unidades=int(numero-miles*1000-centenas*100-decenas*10)
  print(miles,"M +",centenas,"C +",decenas,"D +",unidades,"U")
