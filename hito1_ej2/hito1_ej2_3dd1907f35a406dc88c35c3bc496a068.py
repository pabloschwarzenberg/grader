#Contestador de celular
def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        return True
    elif hora < 14 and numero % 1000 == 909:
        return True
    elif hora >= 17 and hora <= 19 and numero // 1000000 == 877:
        return True
    else:
        return False

numero_telefono = int(input("Ingrese el número telefónico (8 cifras): "))
hora_llamada = int(input("Ingrese la hora de la llamada (0-23): "))

if contestar_llamada(numero_telefono, hora_llamada):
    print("Contestar la llamada")
else:
    print("No contestar la llamada")
      