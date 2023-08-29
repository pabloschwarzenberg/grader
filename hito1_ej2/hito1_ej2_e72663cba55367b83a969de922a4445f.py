def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        return "CONTESTAR"
    elif hora < 14 and numero % 1000 == 909:
        return "CONTESTAR"
    elif hora >= 17 and hora <= 19 and numero // 10000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"

numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

if len(str(numero_telefonico)) != 8:
    print("Número telefónico inválido. Debe tener 8 cifras.")
else:
    resultado = contestar_llamada(numero_telefonico, hora_llamada)

    print("Resultado:", resultado)
