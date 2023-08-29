# Contestador de celular
def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return "CONTESTAR"
    elif hora_llamada < 14 and numero_telefonico % 1000 != 909:
        return "NO CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 10000000 != 877:
        return "NO CONTESTAR"
    elif hora_llamada>=19:
        return "NO CONTESTAR"
    else:
        return "CONTESTAR"

# Solicitar número telefónico y hora de la llamada al usuario
numero = int(input("Ingrese número telefónico: "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

# Obtener el resultado y mostrarlo en pantalla
resultado = contestar_llamada(numero, hora)
print("Resultado:", resultado)

