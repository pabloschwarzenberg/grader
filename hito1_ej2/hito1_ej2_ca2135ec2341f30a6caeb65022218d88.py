def contestar_celular(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero.endswith('909'):
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and numero.startswith('877'):
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar el número telefónico y la hora al usuario
numero_telefonico = input("Ingrese el número telefónico (8 dígitos): ")
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

# Determinar si se debe contestar o no
resultado = contestar_celular(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)