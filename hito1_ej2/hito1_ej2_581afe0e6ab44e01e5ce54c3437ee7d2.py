def contestar_llamada(hora, numero):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 10000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Pedir al usuario la hora y el número de celular
hora = int(input("Ingrese la hora (0-23): "))
numero = int(input("Ingrese el número de celular (8 dígitos): "))

# Llamar a la función y mostrar el resultado
resultado = contestar_llamada(hora, numero)
print(resultado)

# Verificar si se debe contestar la llamada y mostrar el resultado
resultado = contestar_llamada(hora, numero)
print(resultado)

if hora >= 17 and hora < 19 and numero // 10000000 == 877:
        return "CONTESTAR"  # Llamada entre 17:00 y 19:00 y número comienza por 877

    return "NO CONTESTAR"  # Resto de los casos

# Obtener la hora del día y el número de celular desde el usuario
hora = int(input("Ingresa la hora del día (0-23): "))
numero = int(input("Ingresa el número de celular que llama: "))

# Verificar si se debe contestar la llamada y mostrar el resultado
resultado = contestar_llamada(hora, numero)
print(resultado)resultado = contestar_llamada(hora, numero)
print(resultado)