# Diccionario con las fechas de inicio y fin de cada signo zodiacal
fechas_signos = {
    "Aries": ((3, 21), (4, 20)),
    "Tauro": ((4, 21), (5, 20)),
    "Géminis": ((5, 21), (6, 20)),
    "Cáncer": ((6, 21), (7, 22)),
    "Leo": ((7, 23), (8, 22)),
    "Virgo": ((8, 23), (9, 22)),
    "Libra": ((9, 23), (10, 22)),
    "Escorpio": ((10, 23), (11, 21)),
    "Sagitario": ((11, 22), (12, 21)),
    "Capricornio": ((12, 22), (1, 19)),
    "Acuario": ((1, 20), (2, 18)),
    "Piscis": ((2, 19), (3, 20))
}

# Obtener la fecha de nacimiento del usuario
dia_nacimiento = int(input("Ingrese el día de su nacimiento: "))
mes_nacimiento = int(input("Ingrese el mes de su nacimiento: "))

# Comprobar el signo zodiacal
signo_zodiacal = None
for signo, fechas in fechas_signos.items():
    fecha_inicio, fecha_fin = fechas
    if (mes_nacimiento == fecha_inicio[0] and dia_nacimiento >= fecha_inicio[1]) or \
       (mes_nacimiento == fecha_fin[0] and dia_nacimiento <= fecha_fin[1]):
        signo_zodiacal = signo
        break

# Imprimir el resultado
if signo_zodiacal:
    print(signo_zodiacal)
else:
    print("Fecha inválida")
