#Zodiaco
day = int(input("Ingrese su día de cumpleaños (en números): "))
month = int(input("Ingrese su mes de cumpleaños (en números): "))

if 21 < day <= 31 and month == 3 or 1 <= day <= 20 and month == 4:
    print("Aries")
elif 20 < day <= 30 and month == 4 or 1 <= day <= 21 and month == 5:
    print("Tauro")
elif 21 < day <= 31 and month == 5 or 1 <= day <= 21 and month == 6:
    print("Geminis")
elif 21 < day <= 30 and month == 6 or 1 <= day <= 23 and month == 7:
    print("Cancer")
elif 23 < day <= 31 and month == 7 or 1 <= day <= 23 and month == 8:
    print("Leo")
elif 23 < day <= 31 and month == 8 or 1 <= day <= 23 and month == 9:
    print("Virgo")
elif 23 < day <= 30 and month == 9 or 1 <= day <= 23 and month == 10:
    print("Libra")
elif 23 < day <= 31 and month == 10 or 1 <= day <= 22 and month == 11:
    print("Escorpio")
elif 23 <= day <= 30 and month == 11 or 1 <= day <= 22 and month == 12:
    print("Sagitario")
elif 22 < day <= 31 and month == 12 or 1 <= day <= 20 and month == 1:
    print("Capricornio")
elif 20 < day <= 31 and month == 1 or 1 <= day <= 19 and month == 2:
    print("Acuario")
elif 19 < day <= 29 and month == 2 or 1 <= day <= 21 and month == 3:
    print("Piscis") 