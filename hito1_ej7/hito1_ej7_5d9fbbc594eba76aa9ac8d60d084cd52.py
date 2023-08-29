#Zodiaco
dia = int(input("Ingrese de día de nacimiento: "))
mes = int(input("Ingrese de mes de nacimiento: "))

if ((mes==3)and(21<=dia<=31))or((mes==4)and(1<=dia<=19)):
    print("Aries")
elif ((mes==4)and(20<=dia<=30))or((mes==5)and(1<=dia<=20)):
    print("Taurus")
elif ((mes==5)and(21<=dia<=31))or((mes==6)and(1<=dia<=20)):
    print("Gemini")
elif ((mes==6)and(21<=dia<=30))or((mes==7)and(1<=dia<=22)):
    print("Cancer")
elif ((mes==7)and(23<=dia<=31))or((mes==8)and(1<=dia<=22)):
    print("Leo")
elif ((mes==8)and(23<=dia<=31))or((mes==9)and(1<=dia<=22)):
    print("Virgo")
elif ((mes==9)and(23<=dia<=30))or((mes==10)and(1<=dia<=22)):
    print("Libra")
elif ((mes==10)and(23<=dia<=31))or((mes==11)and(1<=dia<=21)):
    print("Escorpio")
elif ((mes==11)and(22<=dia<=30))or((mes==12)and(1<=dia<=21)):
    print("Sagitario")
elif ((mes==12)and(22<=dia<=31))or((mes==1)and(1<=dia<=19)):
    print("Capricornio")
elif ((mes==1)and(20<=dia<=31))or((mes==2)and(1<=dia<=18)):
    print("Acuario")
elif ((mes==2)and(19<=dia<=31))or((mes==3)and(1<=dia<=20)):
    print("Piscis")
