#signos del sodiaco:
#entrada.

dia = int(input("ingrese aquí su mes de nacimiento: "))
mes = int(input("infrese aqui su dia de nacimiento: "))

#Operaciones.

if ((mes==3) and (dia>=21)) or ((mes==4) and (dia<=19)):
    print("aries")
elif ((mes==4) and (dia>=20)) or ((mes==5) and (dia<=20)):
    print("tauro")
elif ((mes==5) and (dia>=21)) or ((mes==6) and (dia<=20)):
    print("geminis")
elif ((mes==6) and (dia>=21)) or ((mes==7) and (dia<=22)):
    print("cancer")
elif ((mes==7) and (dia>=23)) or ((mes==8) and (dia<=22)):
    print("leo")
elif ((mes==8) and (dia>=23)) or ((mes==9) and (dia<=22)):
    print("virgo")
elif ((mes==9) and (dia>=23)) or ((mes==10) and (dia<=22)):
    print("libra")
elif ((mes==10) and (dia>=23)) or ((mes==11) and (dia<=21)):
    print("escorpio")
elif ((mes==11) and (dia>=22)) or ((mes==12) and (dia<=21)):
    print("sagitario")
elif ((mes==12) and (dia>=22)) or ((mes==1) and (dia<=19)):
    print("capricornio")
elif ((mes==1) and (dia>=20)) or ((mes==2) and (dia<=18)):
    print("acuario")
else:
    print("piscis")