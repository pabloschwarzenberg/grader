#Zodiaco

DD = int(input("Ingrese el dia de su nacimiento: "))
MM = int(input("Ingrese el mes de su nacimiento: "))


if DD>=21 and MM==3 or DD<=20 and MM==4:
    print("Su signo es aries")

if DD>=20 and MM==4 or DD<=21 and MM==5:
    print("Su signo es tauro")
    
if DD>=21 and MM==5 or DD<=21 and MM==6:
    print("Su signo es geminis")
    
if DD>=21 and MM==6 or DD<=23 and MM==7:
    print("Su signo es Cancer")
    
if DD>=23 and MM==7 or DD<=23 and MM==8:
    print("Su signo es leo")
    
if DD>=23 and MM==8 or DD<=23 and MM==9:
    print("Su signo es virgo")
    
if DD>=23 and MM==9 or DD<=23 and MM==10:
    print("Su signo es libra")
    
if DD>=23 and MM==10 or DD<=22 and MM==11:
    print("Su signo es escorpio")

if DD>=22 and MM==11 or DD<=22 and MM==12:
    print("Su signo es sagitario")
    
if DD>=22 and MM==12 or DD<=20 and MM==1:
    print("Su signo es capricornio")
    
if DD>=20 and MM==1 or DD<=18 and MM==2:
    print("Su signo es acuario")
    
if DD>=19 and MM==2 or DD<=21 and MM==3:
    print("Su signo es piscis")