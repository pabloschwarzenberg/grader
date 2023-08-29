def contestar_llamada(hora, numero):
    # Verificar si la llamada ocurre entre 00:00 y 07:00
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"

    # Verificar si la llamada ocurre antes de las 14:00
    if hora < 14:
        # Verificar si el número termina en 909
        if numero % 1000 == 909:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"

    # Verificar si la llamada ocurre entre 17:00 y 19:00
    if hora >= 17 and hora <= 19:
        # Verificar si el número comienza por 877
        if numero // 1000000 == 877:
            return "NO CONTESTAR"
        else:
            return "CONTESTAR"

    # Si no se cumple ninguna regla, no contestar
    return "NO CONTESTAR"


# Solicitar la hora y el número telefónico al usuario
hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número telefónico (8 dígitos): "))

# Determinar si se debe contestar la llamada
decision = contestar_llamada(hora, numero)

# Mostrar la decisión en pantalla
print(decision)