#Contestador de celularnumero = int(input("Ingrese número telefónico (8 dígitos): "))
hora = int(input("Ingrese hora de la llamada (0-23): "))

# Verificar si la llamada ocurre entre 00:00 y 07:00
if hora >= 0 and hora < 7:
    print("CONTESTAR")
# Verificar si la llamada ocurre antes de las 14:00
elif hora < 14:
    # Verificar si el número termina en 909
    if numero % 1000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
# Verificar si la llamada ocurre entre 17:00 y 19:00
elif hora >= 17 and hora < 19:
    # Verificar si el número comienza por 877
    if numero // 1000000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
# Si la llamada ocurre después de las 19:00
else:
    print("NO CONTESTAR")
      