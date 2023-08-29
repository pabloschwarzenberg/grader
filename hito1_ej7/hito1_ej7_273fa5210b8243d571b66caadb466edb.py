#Zodiaco

D=int(input("Ingrese su día de su cumpleaños: "))
M=int(input("Ahora ingrese el número del mes de su cumpleaños: "))

if((21<=D<=31) and (M==3)) or((1<=D<=20)and(M==4)):
    print("Aries")

if((21<=D<=30) and (M==4)) or((1<=D<=21) and (M==5)):
    print("Tauro")

if((22<=D<=31) and (M==5)) or((1<=D<=21) and (M==6)):
    print("Geminis")

if((22<=D<=30) and (M==6)) or((1<=D<=22) and (M==7)):
    print("Cancer")

if((23<=D<=31) and (M==7)) or((1<=D<=22) and (M==8)):
    print("Leo")

if((23<=D<=31) and (M==8)) or((1<=D<=23) and (M==9)):
    print("Virgo")

if((24<=D<=30) and (M==9)) or((1<=D<=23) and (M==10)):
    print("Libra")

if((24<=D<=31) and (M==10)) or((1<=D<=22) and (M==11)):
    print("Escorpio")

if((23<=D<=30) and (M==11)) or((1<=D<=21) and (M==12)):
    print("Sagitario")

if((22<=D<=31) and (M==12)) or((1<=D<=20) and (M==1)):
    print("Capricornio")

if((21<=D<=31) and (M==1)) or((1<=D<=19) and (M==2)):
    print("Acuario")

if((20<=D<=29) and (M==2)) or((1<=D<=20) and (M==3)):
    print("Piscis")
