#Contestador de celular
print("Ingrese numero telefonico (8 digitos): ")
numero = input()

hora = int(input("Ingrese Hora de la llamada: "))
if len(numero) == 8:
    if hora >= 0 and hora <= 7:
        print("CONTESTAR")
    elif hora > 7 and hora <= 14 and int(numero[-3:]) == 909:
        print("CONTESTAR")

    elif hora > 7 and hora <= 14:
        print("NO CONTESTAR")
    elif hora >= 17 and hora <= 19 and int(numero[:3]) == 877:
        print("NO CONTESTAR")
    elif hora >= 17 and hora <= 19:
        print("CONTESTAR")
    elif hora > 19:
        print("NO CONTESTAR")  