#Zodiaco
D = int(input("Diga el numero del dia que usted nacio "))
M = int(input("Diga el numero de su mes de nacimiento "))
if D>=21 and M == 3 or D<=20 and M == 4:
    print("Su signo zodiacal es Aries")
elif D>=21 and M == 4 or D<=21 and M == 5:
    print("Su signo zodiacal es Tauro")
elif D>=22 and M == 5 or D<=21 and M == 6:
    print("Su signo zodiacal es Géminis")
elif D>=22 and M == 6 or D<=22 and M == 7:
    print("Su signo zodiacal es Cáncer")
elif D>=23 and M == 7 or D<=23 and M == 8:
    print("Su signo zodiacal es Leo")
elif D>=24 and M == 8 or D<=23 and M == 9:
    print("Su signo zodiacal es Virgo")
elif D>=24 and M == 9 or D<=23 and M == 10:
    print("Su signo zodiacal es Libra")
elif D>=24 and M == 10 or D<=22 and M == 11:
    print("Su signo zodiacal es Escorpión")
elif D>=23 and M == 11 or D<=21 and M == 12:
    print("Su signo zodiacal es Sagitario")
elif D>=22 and M == 12 or D<=20 and M == 1:
    print("Su signo zodiacal es Capricornio")
elif D>=21 and M == 1 or D<=18 and M == 2:
    print("Su signo zodiacal es Acuario")
elif D>=19 and M == 2 or D<=19 and M == 3:
    print("Su signo zodiacal es Piscis")
else:
    print("Su fecha de nacimiento no existe")
    
   