#Zodiaco
# Entradas
day = int(input("Ingrese su dia de nacimiento: "))
month = int(input("Ingrese su mes de nacimiento: "))

# Procesamiento
if month == 1:
    if 20 >= day:
        print("Su signo es Capricornio")
    elif 21 <= day:
        print("Su signo es Acuario")
elif month == 2:
    if 19 >= day:
        print("Su signo es Acuario")
    elif 20 <= day:
        print("Su signo es Piscis")
elif month == 3:
    if 20 >= day:
        print("Su signo es Piscis")
    elif 21 <= day:
        print("Su signo es Aries")
elif month == 4:
    if 21 > day:
        print("Su signo es Aries")
    elif 21 <= day:
        print("Su signo es Tauro")
elif month == 5:
    if 20 >= day:
        print("Su signo es Tauro")
    elif 21 <= day:
        print("Su signo es Geminis")
elif month == 6:
    if 21 >= day:
        print("Su signo es Geminis")
    elif 22 <= day:
        print("Su signo es Cancer")
elif month == 7:
    if 22 >= day:
        print("Su signo es Cancer")
    elif 23 <= day:
        print("Su signo es Leo")
elif month == 8:
    if 23 >= day:
        print("Su signo es Leo")
    elif 24 <= day:
        print("Su signo es Virgo")
elif month == 9:
    if 22 >= day:
        print("Su signo es Virgo")
    elif 23 <= day:
        print("Su signo es Libra")
elif month == 10:
    if 22 >= day:
        print("Su signo es Libra")
    elif 23 <= day:
        print("Su signo es Escorpio")
elif month == 11:
    if 22 >= day:
        print("Su signo es Escorpio")
    elif 23 <= day:
        print("Su signo es Sagitario")
elif month == 12:
    if 21 >= day:
        print("Su signo es Sagitario")
    elif 22 <= day:
        print("Su signo es Capricornio")
        