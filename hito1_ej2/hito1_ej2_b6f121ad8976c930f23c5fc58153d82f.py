#Contestador de celular
# Se solicita al usuario que ingrese el número de teléfono
numero_telefono = int(input("Ingrese el número de teléfono (8 dígitos): "))

# Se solicita al usuario que ingrese la hora del día
hora = int(input("Ingrese la hora del día (0-23): "))

# Verificar si la llamada ocurre entre 00:00 y 07:00
if hora >= 0 and hora < 7:
    print("CONTESTAR")
# Verificar si la llamada ocurre antes de las 14:00, excepto si el número termina en 909
elif hora < 14 and not numero_telefono % 1000 == 909:
    print("NO CONTESTAR")
# Verificar si la llamada ocurre entre 17:00 y 19:00, excepto si el número comienza por 877
elif hora >= 17 and hora < 19 and not numero_telefono // 1000000 == 877:
    print("CONTESTAR")
# No contestar la llamada en cualquier otro caso
else:
    print("NO CONTESTAR")
      