#Contestador de celular
Numero = int(input("Ingrese número telefónico: "))
Hora = int(input("Ingrese hora de la llamada: "))
Final = int(str(Numero)[-3:])
Inicio = int(str(Numero)[:3])

if Hora >= 19:
    print("No contestar")
else:
    if Hora >= 17 and Hora < 19:
        if Inicio == 877:
            print("No contestar")
        else:
            print("Contestar")
    else:
        if Hora < 14:
            if Final == 909:
                print("Contestar")
            else:
                print("No contestar")
        else:
            print("Contestar")
                  