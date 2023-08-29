def contestar_llamada(numero, hora):
    # Comprobar si la llamada ocurre entre 00:00 y 07:00
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    
    # Comprobar si la llamada ocurre antes de las 14:00
    if hora < 14:
        # Comprobar si el número termina en 909
        if numero % 1000 == 909:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    
    # Comprobar si la llamada ocurre entre 17:00 y 19:00
    if hora >= 17 and hora <= 19:
        # Comprobar si el número comienza por 877
        if numero // 10000000 == 877:
            return "CONTESTAR"
        else:
            return "NO CONTESTAR"
    
    # Si la llamada ocurre después de las 19:00
    return "NO CONTESTAR"

# Solicitar al usuario el número telefónico y la hora de la llamada
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

# Obtener el resultado de si contestar o no
resultado = contestar_llamada(numero, hora)

# Imprimir el resultado
print("Resultado:", resultado)
