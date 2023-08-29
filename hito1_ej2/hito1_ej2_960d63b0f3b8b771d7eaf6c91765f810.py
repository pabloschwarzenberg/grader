def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 100 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

# Ejemplo de uso
numero_telefonico = int(input("Ingrese numero telefonico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

resultado = contestar_llamada(numero_telefonico, hora_llamada)
print("Resultado:", resultado)

print("Resultado:", resultado)
