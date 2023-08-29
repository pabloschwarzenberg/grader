#Zodiaco
dia_nacimiento= int(input("Dia de nacimiento: "))
mes_nacimiento= int(input("Mes de nacimiento: "))

if (dia_nacimiento >= 21 and mes_nacimiento == 3) or (dia_nacimiento <= 20 and mes_nacimiento== 4):
    print("ARIES")
   
elif (dia_nacimiento >= 20 and mes_nacimiento == 4) or (dia_nacimiento <= 21 and mes_nacimiento== 5):
    print("TAURO")
   
elif (dia_nacimiento >= 21 and mes_nacimiento == 5) or (dia_nacimiento <= 21 and mes_nacimiento== 6):
    print("GEMINIS")
   
elif (dia_nacimiento >= 21 and mes_nacimiento == 6) or (dia_nacimiento <= 23 and mes_nacimiento== 7):
    print("CANCER")
   
elif (dia_nacimiento >= 23 and mes_nacimiento ==7) or (dia_nacimiento <= 23 and mes_nacimiento== 8):
    print("LEO")
   
elif (dia_nacimiento >= 23 and mes_nacimiento == 8) or (dia_nacimiento <= 23 and mes_nacimiento== 9):
    print("VIRGO")
   
elif (dia_nacimiento >= 23 and mes_nacimiento == 9) or (dia_nacimiento <= 23 and mes_nacimiento== 10):
    print("LIBRA")

elif (dia_nacimiento >= 23 and mes_nacimiento == 10) or (dia_nacimiento <= 22 and mes_nacimiento== 11):
    print("ESCORPIO")

elif (dia_nacimiento >= 23 and mes_nacimiento == 11) or (dia_nacimiento <= 22 and mes_nacimiento== 12):
    print("SAGITARIO")

elif (dia_nacimiento >= 22 and mes_nacimiento == 12) or (dia_nacimiento <= 20 and mes_nacimiento== 1):
    print("CAPRICORNIO")

elif (dia_nacimiento >= 20 and mes_nacimiento == 1) or (dia_nacimiento <= 19 and mes_nacimiento== 2):
    print("ACUARIO")

elif (dia_nacimiento >= 19 and mes_nacimiento == 2) or (dia_nacimiento <= 21 and mes_nacimiento== 3):
    print("PISCIS")
   
else:
    print("Intentar de nuevo")     