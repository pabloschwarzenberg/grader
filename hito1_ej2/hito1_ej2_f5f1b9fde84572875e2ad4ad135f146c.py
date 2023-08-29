#Contestador de celular
hora = int(input("Ingrese la hora actual (0-23): "))
numero = input("Ingrese el número de teléfono que llama (8 dígitos): ")

if len(numero) != 8:
    respuesta = "Este número no es válido"
else:
    numero = int(numero)

    if hora >= 0 and hora <= 7:
        respuesta = "CONTESTAR"
    elif hora == 13 and str(numero) == '77389909':
        respuesta = "CONTESTAR"
    elif hora >= 17 and hora <= 19 and str(numero)[0:3] == "877":
        respuesta = "NO CONTESTAR"
    else:
        respuesta = "NO CONTESTAR"

print(respuesta)      