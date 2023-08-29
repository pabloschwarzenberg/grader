def contestar_telefono(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora < 19 and numero // 100000 == 877:
        return "NO CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar número telefónico y hora de llamada al usuario
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Obtener resultado de contestar o no contestar
resultado = contestar_telefono(numero_telefonico, hora_llamada)

# Imprimir resultado
print("Resultado:", resultado)