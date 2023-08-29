#Zodiaco
Dia = int(input("Ingrese su día de nacimiento: "))
Mes = int(input("Ingrese su mes de nacimiento: "))


if Dia>= 21 and Mes==3 or Dia<=20 and Mes==4:
    print("Aries")
elif Dia>=21 and Mes==4 or Dia<=21 and Mes==5:
    print("Tauro")
elif Dia>=22 and Mes==5 or Dia<=21 and Mes==6:
    print("Geminis")
elif Dia>=22 and Mes==6 or Dia<=23 and Mes==7:
    print("Cancer")
elif Dia>=24 and Mes==7 or Dia<=23 and Mes==8:
    print("Leo")
elif Dia>=24 and Mes==8 or Dia<=23 and Mes==9:
    print("Virgo")
elif Dia>=24 and Mes==9 or Dia<=23 and Mes==10:
    print("Libra")
elif Dia>=24 and Mes==10 or Dia<=22 and Mes==11:
    print("Escorpio")
elif Dia>=23 and Mes==11 or Dia<=22 and Mes==12:
    print("Sagitario")
elif Dia>=23 and Mes==12 or Dia<=20 and Mes==1:
    print("Capricornio")
elif Dia>=21 and Mes==1 or Dia<=19 and Mes==2:
    print("Acuario")
elif Dia>=20 and Mes==2 or Dia<=20 and Mes==3:
    print("Piscis")
else:
    print("Ingrese bien los datos")