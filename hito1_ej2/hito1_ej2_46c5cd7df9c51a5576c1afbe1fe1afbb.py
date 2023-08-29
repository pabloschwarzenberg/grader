#Contestador de celular
numero = int(input("Ingrese un número telefónico: "))
number = str(numero)
numero_de__telefono = list(number)
hora = int(input("Ingrese la hora de llamada: "))

if hora >= 0 and hora <= 7:
    print("¡¡¡CONTESTAR!!!")

elif hora < 14:
    if numero_de__telefono[5] == '9' and numero_de__telefono[6] == '0' and numero_de__telefono[7] == '9':
        print("¡¡¡CONTESTAR!!!")

    else:
        print("NO CONTESTAR!")

elif hora < 17:
    print("NO CONTESTAR")

elif hora >= 17 and hora <= 19:
    if numero_de__telefono[0] == '8' and numero_de__telefono[1] == '7' and numero_de__telefono[2] == '7':
        print("NO CONTESTAR!")

    else:
        print("¡¡¡CONTESTAR!!!")

else:
    print("NO CONTESTAR!")