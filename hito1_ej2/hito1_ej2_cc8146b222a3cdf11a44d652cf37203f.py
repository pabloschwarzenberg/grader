numero_telefono = int(input("Ingrese el número celular: "))
hora_llamada = int(input("Ingrese la hora de la llamada: "))

contador_numeros = len(str(numero_telefono))
residuo = numero_telefono % 1000
residuo = round(residuo)

if contador_numeros == 8 and 0 <= hora_llamada <= 23:
    if 0 <= hora_llamada <= 7:
        print("Contestar")

    elif hora_llamada < 14:
        if residuo == 909:
            print("Contestar")
        else:
            print("No contestar")

    elif 17 <= hora_llamada <= 19:
        if residuo == 877:
            print("Contestar")
        else:
            print("No contestar")

    elif hora_llamada > 19:
        print("No contestar")

else:
    print("Debe ingresar un número celular de 8 dígitos y/o la hora entre 0-23.")