#Contestador de celular
def contestar_llamada(numero, hora):
    # Verificar si la llamada ocurre entre 00:00 y 07:00
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    # Verificar si la llamada ocurre antes de las 14:00
    elif hora < 14:
        # Verificar si el número termina en 909
        if numero % 1000 == 909:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    # Verificar si la llamada ocurre entre 17:00 y 19:00
    elif hora >= 17 and hora < 19:
        # Verificar si el número comienza por 877
        if numero // 100000 == 877:
            return "NO CONTESTAR"
        else:
            return "CONTESTAR"
    # Si la llamada ocurre después de las 19:00
    else:
        return "NO CONTESTAR"


# Solicitar al usuario el número de teléfono y la hora de la llamada
numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Obtener el resultado
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
      