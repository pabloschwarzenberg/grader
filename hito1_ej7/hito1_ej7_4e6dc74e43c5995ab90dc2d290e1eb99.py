#variable
while True:
    d = input("Ingrese día de nacimiento: ")
    m = input("Ingrese mes de nacimiento: ")

    try:
        d = int(d)
        m = int(m)
        if 0 < d <= 31:
            if 0 < m <= 12:
                break
            else:
                print("Mes no valido.")
        else:
            print("Día no valido.")
    except ValueError:
        print("Datos no validos.")

if m == 1:
    if 1 <= d <= 20:
        print("Tú signo es Capricornio.")
    else:
        print("Tú signo es Acuario.")
elif m == 2:
    if 1 <= d <= 19:
        print("Tú signo es Acuario.")
    else:
        print("Tú signo es Piscis.")
elif m == 3:
    if 1 <= d <= 20:
        print("Tú signo es Piscis.")
    else:
        print("Tú signo es Aries.")
elif m == 4:
    if 1 <= d <= 20:
        print("Tú signo es Aries.")
    else:
        print("Tú signo es Tauro.")
elif m == 5:
    if 1 <= d <= 21:
        print("Tú signo es Tauro.")
    else:
        print("Tú signo es Géminis.")
elif m == 6:
    if 1 <= d <= 21:
        print("Tú signo es Géminis.")
    else:
        print("Tú signo es Cáncer.")
elif m == 7:
    if 1 <= d <= 22:
        print("Tú signo es Cáncer.")
    else:
        print("Tú signo es Leo.")
elif m == 8:
    if 1 <= d <= 22:
        print("Tú signo es Leo.")
    else:
        print("Tú signo es Virgo.")
elif m == 9:
    if 1 <= d <= 23:
        print("Tú signo es Virgo.")
    else:
        print("Tú signo es Libra.")
elif m == 10:
    if 1 <= d <= 23:
        print("Tú signo es Libra.")
    else:
        print("Tú signo es Escorpio.")
elif m == 11:
    if 1 <= d <= 22:
        print("Tú signo es Escorpio.")
    else:
        print("Tú signo es Sagitario.")
elif m == 12:
    if 1 <= d <= 21:
        print("Tú signo es Sagitario.")
    else:
        print("Tú signo es Capricornio.")
