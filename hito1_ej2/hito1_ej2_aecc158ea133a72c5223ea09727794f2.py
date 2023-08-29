def contestar_llamada(numero, hora):
    if hora >= 0 and hora <= 7:
        # Llamada entre 00:00 y 07:00
        return True
    elif hora < 14:
        # Llamada antes de las 14:00
        if numero % 1000 == 909:
            # El número termina en 909
            return True
        else:
            return False
    elif hora >= 17 and hora <= 19:
        # Llamada entre 17:00 y 19:00
        if numero // 1000000 == 877:
            # El número comienza por 877
            return True
        else:
            return False
    else:
        # Llamada después de las 19:00
        return False


while True:
    try:
        numero = int(input("Ingresa el número de teléfono (8 dígitos): "))
        hora = int(input("Ingresa la hora de la llamada (0-23): "))
        
        if numero < 10000000 or numero >= 100000000:
            print("El número de teléfono debe tener 8 dígitos.")
        elif hora < 0 or hora > 23:
            print("La hora debe estar entre 0 y 23.")
        else:
            contestar = contestar_llamada(numero, hora)
            if contestar:
                print("CONTESTAR")
            else:
                print("NO CONTESTAR")
            break
        
    except ValueError:
        print("Entrada inválida. Ingresa un número entero.")
      