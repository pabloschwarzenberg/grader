def contestar_llamada(numero_telefono, hora_llamada):
    
    if hora_llamada >= 0 and hora_llamada <= 7:
        return True

    
    if hora_llamada < 14 and numero_telefono % 1000 == 909:
        return True

    
    if hora_llamada >= 17 and hora_llamada <= 19 and numero_telefono // 1000000 == 877:
        return True

    
    return False



numero = int(input("Ingrese el número de teléfono (8 cifras): "))
hora = int(input("Ingrese la hora de la llamada (0-23): "))


if contestar_llamada(numero, hora):
    print("Contestar la llamada.")
else:
    print("No contestar la llamada.")

      