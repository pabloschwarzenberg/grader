#Zodiaco
d=int(input("Ingrese tu dia de nacimiento: "))
m=int(input("Ingrese tu mes de nacimiento: "))
if (m==3 and d>=21) or (m==4 and d<=20) :
    print("Tu signo del zodíaco es Aries")
elif (m==4 and d>=21) or (m==5 and d<=21) :
    print("Tu signo del zodíaco es Tauro")
elif (m==5 and d>=22) or (m==6 and d<=21) :
    print("Tu signo del zodíaco es Géminis")
elif (m==6 and d>=22) or (m==7 and d<=22) :
    print("Tu signo del zodíaco es Cáncer")
elif (m==7 and d>=23) or (m==8 and d<=22) :
    print("Tu signo del zodíaco es Leo")
elif (m==8 and d>=23) or (m==9 and d<=23) :
    print("Tu signo del zodíaco es Virgo")
elif (m==9 and d>=24) or (m==10 and d<=23) :
    print("Tu signo del zodíaco es Libra")
elif (m==10 and d>=24) or (m==11 and d<=22) :
    print("Tu signo del zodíaco es Escorpio")
elif (m==11 and d>=23) or (m==12 and d<=21) :
    print("Tu signo del zodíaco es Sagitario")
elif (m==12 and d>=22) or (m==1 and d<=20) :
    print("Tu signo del zodíaco es Capricornio")
elif (m==1 and d>=21) or (m==2 and d<=19) :
    print("Tu signo del zodíaco es Acuario")
else :
    print("Tu signo del zodíaco es Piscis")
