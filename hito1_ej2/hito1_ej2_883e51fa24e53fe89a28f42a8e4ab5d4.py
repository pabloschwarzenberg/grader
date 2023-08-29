# Pedimos el número telefónico y la hora al usuario
numero = int(input("Ingrese el número telefónico (8 cifras): "))
hora = int(input("Ingrese la hora de la llamada (0-23): "))

# Verificamos las reglas para contestar o no la llamada
if hora >= 0 and hora <= 7:
    # Si la llamada ocurre entre 00:00 y 07:00, la contestamos
    print("CONTESTAR")
elif hora < 14:
    # Si ocurre antes de las 14:00 no la contestamos, excepto si el número termina en 909
    if numero % 1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora >= 17 and hora <= 19:
    # Durante la tarde, solamente contestamos entre 17:00 y 19:00, exceptuando un número que comienza por 877
    if numero // 100000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
else:
    # Después de las 19:00, no contestamos el celular
    print("NO CONTESTAR")
      