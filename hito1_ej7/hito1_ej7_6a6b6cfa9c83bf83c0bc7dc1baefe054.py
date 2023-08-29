#Zodiaco
D=int(input("Ingrese el dia de su nacimiento: "))
M=int(input("Ingrese su mes de nacimiento: "))

if (M==3 and D>=21)or(M==4 and D<=20):
    print("aries")
elif (M==4 and D>=21)or(M==5 and D<=21):
    print("taur9")
elif (M==5 and D>=22)or(M==6 and D<=21):
    print("gemini")
elif (M==6 and D>=22)or(M==7 and D<=22):
    print("cancer")
elif (M==7 and D>=23)or(M==8 and D<=22):
    print("leo")
elif (M==8 and D>=23)or(M==9 and D<=23):
    print("virgo")
elif (M==9 and D>=24)or(M==10 and D<=23):
    print("libra")
elif (M==10 and D>=24)or(M==11 and D<=22):
    print("escorpio")
elif (M==11 and D>=23)or(M==12 and D<=21):
    print("sagitario")
elif (M==12 and D>=22)or(M==1 and D<=20):
    print("capricornio")
elif (M==1 and D>=21)or(M==2 and D<=19):
    print("acuario")
elif (M==2 and D>=20)or(M==3 and D<=20):
    print("piscis")