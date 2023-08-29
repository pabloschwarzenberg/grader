#Escribe un programa que reciba tres números enteros y los imprima ordenados de menor a mayor, separados por una coma.
primero= eval(input("ingrese el primer número: "))
segundo= eval(input("ingrese el segundo número: "))
tercero= eval(input("ingrese el tercer número: "))
#ordenar números de menor a mayor
if(primero<=segundo<=tercero):
  print("el orden de menor a mayor es: ",primero, ",", segundo, ",", tercero)
if(primero<=tercero<=segundo):
  print("el orden de menor a mayor es: ",primero, ",", tercero, ",", segundo)
if(segundo<=tercero<=primero):
  print("el orden de menor a mayor es: ",segundo, ",", tercero, ",", primero)
if(segundo<=primero<=tercero): 
  print("el orden de menor a mayor es: ",segundo, ",", primero, ",", tercero)
if(tercero<=segundo<=primero):
  print("el orden de menor a mayor es: ",tercero, ",", segundo, ",", primero)
if(tercero<=primero<=segundo):
  print("el orden de menor a mayor es: ",tercero, ",", primero, ",", segundo)