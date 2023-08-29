def contestar_llamada(numero_telefonico, hora_llamada):
    if hora_llamada >= 0 and hora_llamada < 7:
        return True
    if hora_llamada < 14 and numero_telefonico % 100 != 909:
        return True
    if hora_llamada >= 17 and hora_llamada < 19 and numero_telefonico // 1000000 == 877:
        return True
    return False
# Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico: "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))
# Verificar si se debe contestar o no la llamada
if contestar_llamada(numero_telefonico, hora_llamada):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")