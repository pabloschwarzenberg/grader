print("Hola buenas, ingresa tus datos para que te indique cual es tu signo")
print ("ingrese el dia que nacio")
dia=int(input())
print(" ingrese el mes que nacio")
mes=(input(""))

if((dia>=20 and mes=="3") or (dia<=21 and mes=="4")):
    print("tu signo es aries")
elif((dia>=20 and mes=="4") or (dia<=20 and mes=="5")):
    print("tu signo es tauro")
elif((dia>=21 and mes=="5") or (dia<=21 and mes=="6")):
    print("tu signo es gemenis")
elif((dia>=22 and mes=="6") or (dia<=21 and mes=="7")):
    print("tu signo es cancer")
elif((dia>=22 and mes=="7") or (dia<=22 and mes=="8")):
    print("tu signo es leo")
elif((dia>=23 and mes=="8") or (dia<=22 and mes=="9")):
    print("tu signo es virgo")
elif((dia>=23 and mes=="9") or (dia<=22 and mes=="10")):
    print("tu signo es libra")
elif((dia>=23 and mes=="10") or (dia<=22 and mes=="11")):
    print("tu signo es escorpio")
elif((dia>=23 and mes=="11") or (dia<=22 and mes=="12")):
    print("tu signo es sagitario")
elif((dia>=23 and mes=="12") or (dia<=21 and mes=="1")):
    print("tu signo es capricornio")
elif((dia>=22 and mes=="1") or (dia<=17 and mes=="2")):
    print("tu signo es acuario")
elif((dia>=18 and mes=="2") or (dia<=19 and mes=="3")):
    print("tu signo es piscis")