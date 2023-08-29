#Zodiaco
Dia = int(input("mencione el dia: "))
MES = int(input("mencione el mes: "))
if MES > 12 or MES == 0 or MES < 0:
    print("El mes no puede ser mayor a 12, o igual a cero o menor a cero, intentelo nuevamente: ")
elif  (Dia > 31) or (Dia == 0) or (Dia > 28 and MES == 2 ) or (Dia > 30 and MES == 4) or (Dia > 30 and MES == 6) or (Dia > 30 and MES == 9) or (Dia > 30 and MES == 11) or (Dia < 0):
    print("Ese dia no existe en el calendario")
else:
    if (Dia >= 21 and MES == 3) or (Dia < 20 and MES == 4):
        print("tu signo es ARIES")
    elif (Dia >= 20 and MES == 4) or (Dia < 21 and MES == 5):
        print("tu signo es Tauro")
    elif (Dia >= 21 and MES == 5) or (Dia < 21 and MES == 6):
        print("tu signo es Geminis")
    elif (Dia >= 21 and MES == 6) or (Dia < 23 and MES == 7):
        print("tu signo es Cancer")
    elif (Dia >= 23 and MES == 7) or (Dia < 23 and MES == 8):
        print("tu signo es León")
    elif (Dia >= 23 and MES == 8) or (Dia < 23 and MES == 9):
        print("tu signo es Virgo")
    elif (Dia >= 23 and MES == 9) or (Dia < 23 and MES == 10):
        print("tu signo es Libra")
    elif (Dia >= 23 and MES == 10) or (Dia <= 22 and MES == 11):
        print("tu signo es Escorpión")
    elif (Dia >= 23 and MES == 11) or (Dia < 22 and MES == 12):
        print("tu signo es Sagitario")
    elif (Dia >= 22 and MES == 12) or (Dia < 20 and MES == 1):
        print("tu signo es Capricornio")
    elif (Dia >= 20 and MES == 1) or (Dia < 19 and MES == 2):
        print("tu signo es Acuario")
    elif (Dia >= 19 and MES == 2) or (Dia < 21 and MES == 3):
        print("tu signo es Piscis")   