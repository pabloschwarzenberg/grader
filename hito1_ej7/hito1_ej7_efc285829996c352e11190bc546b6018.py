dia=int(input("Digite su dia de nacimiento: "))
mes=int(input("Digite su mes de nacimiento: "))
while not mes>=1 and mes<=12:
    mes = int(input("Error, digite un mes de nacimiento valido"))

if (mes==3 and dia>=21) or (mes==4 and dia<=20):
    print("Aries")
elif (mes==4 and dia>=20) or (mes==5 and dia<=21):
    print("Tauro")
elif (mes==5 and dia>=21) or (mes==6 and dia<=21):
    print("Gemini")
elif (mes==6 and dia>=21) or (mes==7 and dia<=23):
    print("Cancer")
elif (mes==7 and dia>=23) or (mes==8 and dia<=23):
    print("Leo")
elif (mes==8 and dia>=23) or (mes==9 and dia<=23):
    print("Virgo")
elif (mes==9 and dia>=23) or (mes==10 and dia<=23):
    print("Libra")
elif (mes==10 and dia>=23) or (mes==11 and dia<=22):
    print("Escorpio")
elif (mes==11 and dia>=22) or (mes==12 and dia<=22):
    print("Sagitario")
elif (mes==12 and dia>=22) or (mes==1 and dia<=20):
    print("Capricornio")
elif (mes==1 and dia>=20) or (mes==2 and dia<=19):
    print("Acuario")
elif (mes==2 and dia>=19) or (mes==3 and dia<=21):
    print("Piscis")