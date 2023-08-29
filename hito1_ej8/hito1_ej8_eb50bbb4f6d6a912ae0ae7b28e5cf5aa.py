numero = input("ingrese un numero: ")
if len(numero) == 4:
  print(numero[0]+str("M")+str("+")+numero[1]+str("C")+str("+")+numero[2]+str("D")+str("+")+numero[3]+str("U"))


if len(numero) == 3:
  print(numero[0]+str("C")+str("+")+numero[1]+str("D")+str("+")+numero[2]+str("U"))


if len(numero) == 2:
  print(numero[0]+str("D")+str("+")+numero[1]+str("U"))

if len(numero) == 1:
  print(numero[0]+str("U"))