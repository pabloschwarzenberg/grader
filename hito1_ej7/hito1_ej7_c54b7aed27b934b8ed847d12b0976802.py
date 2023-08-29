#Zodiaco
dia=int(input("ingrese el dia de su nacimiento: \n"))
mes=int(input("ingrese el mes de su nacimiento: \n"))

def signo(d,m):
    if (d>=21 and m==3) or (d<=20 and m==4):
        return "Aries"
    elif (d>=21 and m==4) or (d<=21 and m==5):
        return "Taurus"
    elif (d>=22 and m==5) or (d<=21 and m==6):
        return "Gemini"
    elif (d>=22 and m==6) or (d<=22 and m==7):
        return "Cancer"
    elif (d>=23 and m==7) or (d<=22 and m==8):
        return "Leo"
    elif (d>=23 and m==8) or (d<=23 and m==9):
        return "Virgo"
    elif (d>=24 and m==9) or (d<=23 and m==10):
        return "Libra"
    elif (d>=24 and m==10) or (d<=22 and m==11):
        return "escorpio"
    elif (d>=23 and m==11) or (d<=21 and m==12):
        return "Sagittarius"
    elif (d>=22 and m==12) or (d<=20 and m==1):
        return "Capricorn"
    elif (d>=21 and m==1) or (d<=19 and m==2):
        return "Aquarius"
    elif (d>=20 and m==2)or(d<=20 and m==3):
        return "Pisces"
a=signo(dia,mes)        
print ("su signo del zodiaco es: "+str(a))    
     