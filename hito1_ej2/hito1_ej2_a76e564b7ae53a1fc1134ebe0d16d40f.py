#Contestador de celular
def contestar_celular(numero, hora):
    # Verificar si la llamada ocurre entre 00:00 y 07:00
    if hora >= 0 and hora < 7:
        return "CONTESTAR"

    # Verificar si la llamada ocurre antes de las 14:00
    if hora < 14:
        # Verificar si el número termina en 909
        if numero % 1000 == 909:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"

    # Verificar si la llamada ocurre entre 17:00 y 19:00
    if hora >= 17 and hora < 19:
        # Verificar si el número comienza por 877
        if numero // 1000000 == 877:
            return "NO CONTESTAR"
        else:
            return "NO CONTESTAR"

    # Llamada después de las 19:00
    return "NO CONTESTAR"


# Obtener el número de teléfono y la hora de la llamada
numero = int(input("Ingrese numero telefonico: "))
hora = int(input("Ingrese hora de la llamada: "))

# Obtener el resultado y mostrarlo en pantalla
resultado = contestar_celular(numero, hora)
print("Resultado:", resultado)
