#Zodiaco
D=int(input("Ingresa tu día de nacimiento:"))
M=int(input("Ingresa tu mes de nacimiento(en números):"))
if (M==3 and D>= 24) or (M==4 and D<=21):
    print("Tu signo es Aries")
elif (M==4 and D>=22) or (M==5 and D<=21):
    print("Tu signo es Tauro")
elif (M==5 and D>=22) or (M==6 and D<=21):
    print("Tu signo es Géminis")
elif (M==6 and D>=22) or (M==7 and D<=21):
    print("Tu signo es Cáncer")
elif (M==7 and D>=22) or (M==8 and D<=22):
    print("Tu signo es Leo")
elif (M==8 and D>=23) or (M==9 and D<=21):
    print("Tu signo es Virgo")
elif (M==9 and D>=22) or (M==10 and D<=21):
    print("Tu signo es Libra")
elif (M==10 and D>=22) or (M==11 and D<=22):
    print("Tu signo es Escorpio")
elif (M==11 and D>=23) or (M==12 and D<=21):
    print("Tu signo es Sagitario")
elif (M==12 and D>=22) or (M==1 and D<=21):
    print("Tu signo es Capricornio")
elif (M==1 and D>=22) or (M==2 and D<=21):
    print("Tu signo es Acuario")
elif (M==2 and D>=22) or (M==3 and D<=23):
    print("Tu signo es Piscis")