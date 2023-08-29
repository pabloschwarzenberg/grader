#Descomponer un número
numero = input( "ingrese numero de cuatro digitos",)
largo = len(numero)
if largo == 1:
  unidad = str(numero[0] + "U")
  print(unidad)
if largo == 2:
  decena = str(numero[0] + "D")
  unidad = str(numero[1] + "U")
  print(decena,"+",unidad)  
if largo == 3:
  centena = str(numero[0] + "C")
  decena = str(numero[1] + "D")
  unidad = str(numero[2] + "U")
  print(centena, "+", decena,"+", unidad)
if largo == 4:
  miles = str(numero[0] + "M")
  centena = str(numero[1] + "C")
  decena = str(numero[2] + "D")
  unidad = str(numero[3] + "U")
  print(miles,"+", centena, "+", decena,"+", unidad)
