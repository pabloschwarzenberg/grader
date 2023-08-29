#Descomponer un número
numero = input("ingrese su numero de hasta 4 digitos: ")

if len(numero)==1:
    unidad= numero[0]

    print(unidad,"U")

elif len(numero)==2:
    unidad= numero[1]
    decena= numero[0]

    print(decena,"D","+", unidad,"U")

elif len(numero)==3:
    unidad= numero[2]
    decena= numero[1]
    centena= numero[0]

    print(centena,"C","+", decena,"D","+", unidad,"U")

elif len(numero)==4:
    milesima = numero[0]
    centena= numero[1]
    decena= numero[2]
    unidad= numero[3]

    print(milesima,"M", "+", centena,"C", "+", decena,"D", "+", unidad,"U")