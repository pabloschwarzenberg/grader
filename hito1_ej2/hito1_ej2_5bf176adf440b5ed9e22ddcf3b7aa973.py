#Contestador de celular
def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return "CONTESTAR"
    elif hora < 14 and not numero.endswith('909'):
        return "NO CONTESTAR"
    elif hora >= 17 and hora < 19 and not numero.startswith('877'):
        return "NO CONTESTAR"
    else:
        return "CONTESTAR"

# Solicitar número de teléfono y hora al usuario
numero_telefonico = input("Ingrese número telefónico (8 dígitos): ")
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Determinar si se debe contestar o no
resultado = contestar_llamada(numero_telefonico, hora_llamada)

# Imprimir el resultado
print("Resultado:", resultado)
      