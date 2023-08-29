def contestar_celular(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and str(numero)[-3:] == "909":
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and str(numero)[:3] == "877":
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar entrada al usuario
hora_actual = int(input("Ingrese la hora actual (0-23): "))
numero_telefono = int(input("Ingrese el número de teléfono (8 dígitos): "))

# Llamar a la función para determinar si se contesta o no
respuesta = contestar_celular(hora_actual, numero_telefono)

# Imprimir la respuesta
print(respuesta)
