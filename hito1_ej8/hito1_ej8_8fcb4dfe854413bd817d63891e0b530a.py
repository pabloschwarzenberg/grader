#Descomponer un número
numero = input("ingrese un numero: ")
if(len(numero)==4):
    mil = numero[0:1]
    centena = numero[1:2]
    decena = numero[2:3]
    unidad = numero[3:4]
    print(mil, "M", "+", centena, "C", "+", decena, "D", "+", unidad, "U")

elif(len(numero)==3):
    centena = numero[0:1]
    decena = numero[1:2]
    unidad = numero[2:3]
    print(centena,"C", "+" ,decena,"D", "+" ,unidad,"U")

elif(len(numero)==2):
    decena = numero[0:1]
    unidad = numero[1:2]
    print(decena, "D", "+", unidad, "U")

elif(len(numero)==1):
    unidad = numero[0:1]
    print(unidad, "U")      