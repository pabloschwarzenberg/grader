def contestar_llamada(hora, numero):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"  # Si la llamada ocurre entre 00:00 y 07:00, la contestas
    elif hora < 14 and str(numero)[-3:] == "909":
        return "CONTESTAR"  # Si ocurre antes de las 14:00, la contestas si el número termina en 909
    elif hora >= 17 and hora < 19 and str(numero).startswith("877"):
        return "NO CONTESTAR"  # Durante la tarde, solamente contestas entre 17:00 y 19:00 si el número comienza por 877
    else:
        return "NO CONTESTAR"  # Después de las 19:00, no contestas el celular


# Solicitar al usuario ingresar el número de celular y la hora de la llamada
numero_telefonico = input("Ingrese el número de celular: ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Determinar si se debe contestar la llamada
decision = contestar_llamada(hora_llamada, numero_telefonico)

# Imprimir la decisión
print("Resultado:", decision)

      