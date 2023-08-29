#Zodiaco
D = int(input("Escriba su dia de nacimiento -> "))
M = int(input("Escriba su mes de nacimiento -> "))


if (D>=21 and M==3) or (D<=20 and M==4) :
    S=("Aries")

if (D >= 21 and M==4) or (D<=21 and M==5):
    S=("Tauro")

if (D>=2 and M==5) or (D<=21 and M==6):
    S=("Geminis")

if (D>=21 and M==6) or (D<=23 and M==7):
    S = ("Cáncer")

if (D>=23 and M==7) or (D<=23 and M==8):
    S=("Leo")

if (D>=23 and M==8) or (D<=23 and M==9):
    S=("Virgo")

if (D>=23 and M==9) or (D<=22 and M==10):
    S=("Libra")

if (D>=23 and M==10) or (D<=22 and M==11):
    S=("Escorpio")

if (D>=23 and M==11) or (D<=22 and M==12):
    S=("Sagitario")

if (D>=22 and M==12) or (D<=20 and M==1):
    S=("Capricornio")

if (D>=20 and M==1) or (D<=19 and M==2):
    S=("Acuario")

if (D>=19 and M==2) or (D<=21 and M==3):
    S=("Piscis")

print("Su signo zodiacal es: ", S)