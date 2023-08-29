#Contestador de celular
NumeroCelular = input("Ingrese numero telefonico ")
Hora = int(input("Ingrese hora de la llamada "))

if Hora >= 0 and Hora <= 7:
    print("CONTESTAR")
elif Hora < 14:
    print("CONTESTAR")
elif NumeroCelular[8-3:] == 909:
    print("CONTESTAR")
elif Hora >= 17 and Hora <= 19:
    if NumeroCelular[0:3] == 877:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif Hora > 19:
    print("NO CONTESTAR")

