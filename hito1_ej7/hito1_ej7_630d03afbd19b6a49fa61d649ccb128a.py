#Zodiaco
dia = eval(input("Ingrese el dia de cumpleaños: "))
mes = eval(input("Ingrese el mes de cumpleaños (en numeros): "))

if (21 <= dia <= 31) and (mes == 3) or (20 > dia > 0) and (mes == 4):
    print("Aries")
elif (20 <= dia <= 31) and (mes == 4) or (21 > dia > 0) and(mes == 5):
    print("Taurus")
elif (21 <= dia <= 31) and (mes == 5) or (21 > dia > 0) and (mes == 6):
    print("Gemini")
elif (21 <= dia <= 31) and (mes == 6) or (23 > dia > 0) and (mes == 7):
    print("Cancer")
elif (23 <= dia <= 31) and (mes == 7) or (23 > dia > 0) and (mes == 8):
    print("Leo")
elif (23 <= dia <= 31) and (mes == 8) or (23 > dia > 0) and (mes == 9):
    print("Virgo")
elif (23 <= dia <= 31) and (mes == 9) or (23 > dia > 0) and (mes == 10):
    print("Libra")
elif (23 <= dia <= 31) and (mes == 10) or (22 > dia > 0) and (mes == 11):
    print("Escorpio")
elif (22 <= dia <= 31) and (mes == 11) or (22 > dia > 0) and (mes == 12):
    print("Sagitario")
elif (22 <= dia <= 31) and (mes == 12) or (20 > dia > 0) and (mes == 1):
    print("Capricornio")
elif (20 <= dia <= 31) and (mes == 1) or (19 > dia > 0) and (mes == 2):
    print("Acuario")
elif (19 <= dia <= 31) and (mes == 2) or (21 > dia > 0) and (mes == 3):
    print("Pisces")
else:
    print("Esa fecha no eñiste")