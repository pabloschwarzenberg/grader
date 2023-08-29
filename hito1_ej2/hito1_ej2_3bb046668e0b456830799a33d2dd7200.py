def contestar_telefono(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada <= 7:
        return "CONTESTAR"
    elif hora_llamada <= 14 or numero_telefonico % 100 == 909:
        return "CONTESTAR"
    elif hora_llamada >= 17 and hora_llamada <= 19 and numero_telefonico // 1000000 == 877:
        return "CONTESTAR"
    else:
        return "NO CONTESTAR"
numero = int(input("Ingrese número telefónico (8 cifras): "))
hora = int(input("Ingrese hora de la llamada (0-23): "))
resultado = contestar_telefono(numero, hora)
print(resultado)