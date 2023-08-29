def contestar_celular(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Solicitar número telefónico y hora de la llamada al usuario
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada: "))

# Determinar si se debe contestar o no
resultado = contestar_celular(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)


