#Descomponer un número
numero = input("numero de 4 cifras: ")
contador = len(numero)

if contador == 4:
    miles = numero[-4] + "M + "
    centena = numero[-3] + "C + "
    decena = numero[-2] + "D + "
    unidad = numero[-1] + "U"
    print(miles + centena + decena + unidad)

elif contador == 3:
    centena = numero[-3] + "C + "
    decena = numero[-2] + "D + "
    unidad = numero[-1] + "U"
    print(centena + decena + unidad)
    
elif contador == 2:
    decena = numero[-2] + "D + "
    unidad = numero[-1] + "U"
    print(decena + unidad)
    
elif contador == 1:
    unidad = numero[-1] + "U"
    print(unidad)