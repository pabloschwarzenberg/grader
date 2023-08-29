#Descomponer un número
from os import system
system('cls')

#entrada
number = str(input("Ingrese un número de HASTA 4 dígitos: "))
print("Su número es", number + ".")

# proceso
i = len(str(number))

if i == 1:
    unidad = str(number)
    print(unidad + "U")

elif i == 2:
    unidad = str(number[1])
    decena = str(number[0])
    print(decena + "D", "+", unidad + "U")

elif i == 3:
    unidad = str(number[2])
    decena = str(number[1])
    centena = str(number[0])
    print(centena + "C", "+", decena + "D", "+", unidad + "U")

elif i == 4:
    unidad = str(number[3])
    decena = str(number[2])
    centena = str(number[1])
    umil = str(number[0])
    print(umil + "M", "+", centena + "C", "+", decena + "D", "+", unidad + "U")