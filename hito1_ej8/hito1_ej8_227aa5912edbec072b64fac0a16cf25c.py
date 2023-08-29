#Descomponer un número
      #Escribe un programa que le pida al usuario un número de hasta 4 dígitos y que te entregue
#la descomposición en Unidades, Decenas, Centenas y Miles.

numero = int(input(" ingrese un numero de 4 digitos: "))
largo = len(str(numero))

if largo > 4:
    print("Su numero debe ser de 4 digitos")
else:
    unidad = 1
    letra = ""
    resultado = ""
    while largo > 0:
        if unidad==1:
            letra= "U"
        elif unidad == 2:
            letra = "D"
        elif unidad == 3:    
            letra = "C"
        elif unidad ==4:
            letra = "UM"
        unidad += 1
        largo = largo -1
        resultado = "+" + str(numero)[largo] + letra + resultado

    print(" su resultado: ",resultado[1:])