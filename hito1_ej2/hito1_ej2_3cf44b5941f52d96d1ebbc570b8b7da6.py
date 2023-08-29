NT = int(input("Ingrese el número de celular (8 dígitos): "))
HL = int(input("Ingrese la hora (0-23): "))

# Verificar si la llamada ocurre entre 00:00 y 07:00
if (HL>=00 and HL<7):
    print("CONTESTAR")

# Verificar si la llamada ocurre antes de las 14:00, excepto si el número termina en 909
elif (HL<14 and NT==77389909):
    print("CONTESTAR")

# Verificar si la llamada ocurre entre 17:00 y 19:00, excepto si el número comienza por 877
elif (HL>=17 and HL<19 and NT==87765545):
    print("NO CONTESTAR")
# No contestar después de las 19:00
else:
    print("NO CONTESTAR")