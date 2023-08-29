#Descomponer un número
#Entrada
Num = int(input("Ingrese número de hasta 4 dígitos: "))

#Procedimiento
if 0 < Num < 10000:
  mil  = Num//1000
  centena = (Num % 1000)//100
  decena = ((Num % 1000)%100)//10
  unidad = ((Num % 1000)%100)%10
  print(mil,"M +", centena, "C +", decena, "D +", unidad, "U +")
else:
  print("Debe ser un número de solo 4 dígitos")
  
