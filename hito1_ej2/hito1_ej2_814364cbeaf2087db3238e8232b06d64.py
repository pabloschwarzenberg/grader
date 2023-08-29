def contestador_automatico(numero, hora):
    if hora >= 0 and hora < 7:
        return True
    elif hora < 14 and numero % 1000 == 909:
        return True
    elif hora >= 17 and hora < 19 and numero // 10000000 == 877:
        return True
    else:
        return False

numero = int(input("Ingresa un numero telefonico: "))
hora = int(input("Ingresa la hora de llamada: "))

if contestador_automatico(numero, hora):
    print("Resultado: CONTESTAR")
else:
    print("Resultado: NO CONTESTAR")