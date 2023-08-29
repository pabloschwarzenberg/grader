day = int(input("Ingresa el dia de nacimiento"))
month = int(input("Ingresa el mes de nacimiento"))
if((12 >= month >= 1) and (31 >= day >= 1)):
    if((month == 3 and day >= 21) or (month == 4 and day <= 20)):
        print("Aries")
    elif((month == 4 and day >= 20) or (month == 5 and day <= 21)):
        print("Tauro")
    elif((month == 5 and day >= 21) or (month == 6 and day <= 21)):
        print("Geminis")
    elif((month == 6 and day >= 21) or (month == 7 and day <= 23)):
        print("Cancer")
    elif((month == 7 and day >= 23) or (month == 8 and day <= 23)):
        print("Leo")
    elif((month == 8 and day >= 23) or (month == 9 and day <= 23)):
        print("Virgo")
    elif((month == 9 and day >= 23) or (month == 10 and day <= 23)):
        print("Libra")
    elif((month == 10 and day >= 23) or (month == 11 and day <= 22)):
        print("Escorpio")
    elif((month == 11 and day >= 23) or (month == 12 and day <= 22)):
        print("Sagitario")
    elif((month == 12 and day >= 22) or (month == 1 and day <= 20)):
        print("Capricornio")
    elif((month == 1 and day >= 20) or (month == 2 and day <= 19)):
        print("Acuario")
    elif((month == 2 and day >= 19) or (month == 3 and day <= 21)):
        print("Piscis")
    else:
        print("Error en las fechas.")
else:
    print("Error en las fechas.")