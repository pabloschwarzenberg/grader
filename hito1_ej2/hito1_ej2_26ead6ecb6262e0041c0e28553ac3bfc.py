def contestar_llamada(numero_telefonico, hora_llamada):
    # Verificar si la llamada ocurre entre 00:00 y 07:00
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"

    # Verificar si la llamada ocurre antes de las 14:00
    if hora_llamada < 14:
        # Verificar si el número termina en 909
        if numero_telefonico % 1000 == 909:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"

    # Verificar si la llamada ocurre entre 17:00 y 19:00
    if hora_llamada >= 17 and hora_llamada < 19:
        # Verificar si el número comienza por 877
        if str(numero_telefonico)[0:3] == "877":
            return "NO CONTESTAR"

    # Si ninguna de las condiciones anteriores se cumple, no contestar
    return "NO CONTESTAR"


# Solicitar al usuario ingresar el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Llamar a la función para determinar si se debe contestar o no
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado en pantalla
print("Resultado:", resultado)
