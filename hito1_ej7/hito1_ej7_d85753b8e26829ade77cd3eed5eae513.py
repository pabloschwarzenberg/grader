#Zodiaco
D =int(input("Ingrese su dia de nacimiento "))
M =int(input("Ingrese su mes de nacimiento "))

if D>=21 and M==3 or D<=20 and M==4:
    print(" tu signo del zodiaco es Aries")
elif D>=21 and M==4 or D<=21 and M==5:
    print(" tu signo del zodiaco es Tauro")
elif D>=22 and M==5 or D<=21 and M==6:
    print(" tu signo del zodiaco es Geminis")
elif D>=22 and M==6 or D<=22 and M==7:
    print(" tu signo del zodiaco es Cancer")
elif D>=23 and M==7 or D<=23 and M==8:
    print(" tu signo del zodiaco es Leo")
elif D>=24 and M==8 or D<=23 and M==9:
    print(" tu signo del zodiaco es Virgo")
elif D>=24 and M==9 or D<=23 and M==10:
    print(" tu signo del zodiaco es Libra")
elif D>=24 and M==10 or D<=22 and M==11:
    print(" tu signo del zodiaco es Escorpion")
elif D>=23 and M==11 or D<=21 and M==12:
    print(" tu signo del zodiaco es Sagitario")
elif D>=22 and M==12 or D<=20 and M==1:
    print(" tu signo del zodiaco es Capricornio")
elif D>=21 and M==1 or D<=18 and M==2:
    print(" tu signo del zodiaco es Acuario")
elif D>=19 and M==2 or D<=20 and M==3:
    print(" tu signo del zodiaco es Piscis")
else:
    print("Infrese bien su fecha de nacimiento")      