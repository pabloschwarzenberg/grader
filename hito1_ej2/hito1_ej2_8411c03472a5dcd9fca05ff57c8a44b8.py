#Contestador de celular
def contestar_llamada(numero, hora):
    if hora >= 0 and hora < 7:
        return True
    elif hora < 14:
        if numero % 1000 == 909:
            return True
        else:
            return False
    elif hora >= 17 and hora < 19:
        if str(numero)[0:3] != '877':
            return True
        else:
            return False
    else:
        return False

# Solicitar al usuario el número telefónico y la hora de la llamada
numero_telefonico = int(input("Ingrese número telefónico (8 dígitos): "))
hora_llamada = int(input("Ingrese hora de la llamada (0-23): "))

# Determinar si debes contestar la llamada
if contestar_llamada(numero_telefonico, hora_llamada):
    print("CONTESTAR")
else:
    print("NO CONTESTAR")
