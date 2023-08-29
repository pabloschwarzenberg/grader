#Sistema de Ecuaciones
num1 = int(input("ingrese la variable que acompaña a la primera X -> "))
num2 = int(input("ingrese la variable que acompaña a la primera Y -> "))
num3 = int(input("ingrese la variable de la primera igualación -> "))
num4 = int(input("ingrese l variable que acompaña a la segunda X -> "))
num5 = int(input("ingrese la variable que acompaña a la segunda Y -> "))
num6 = int(input("ingrese la variable de la segunda igualación -> "))

procesoY = ((num6*num1)-(num4*num3))/((num1*num5)-(num4*num2))

procesoX = (num3-num2*procesoY)/num1

print("x =",procesoX,", y =",procesoY)      