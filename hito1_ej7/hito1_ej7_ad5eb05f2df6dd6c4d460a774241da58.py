#Zodiaco
dia=int(input("Que dia nacio: "))
mes=int(input("Que mes nacio(poner el numero): "))
if (mes==3 and dia>=21) or (mes==4 and dia<=19):
    simbolo="Aries"
elif (mes==4 and dia>=20) or (mes==5 and dia<=20):
    simbolo="Tauro"
elif (mes==5 and dia>=21) or (mes==6 and dia<=20):
    simbolo="Geminis"
elif (mes==6 and dia>=21) or (mes==7 and dia<=22):
    simbolo="Cancer"
elif (mes==7 and dia>=23) or (mes==8 and dia<=22):
    simbolo="Leon"
elif (mes==8 and dia>=23) or (mes==9 and dia<=22):
    simbolo="Virgo"
elif (mes==9 and dia>=23) or (mes==10 and dia<=22):
    simbolo="Libra"
elif (mes==10 and dia>=23) or (mes==11 and dia<=21):
    simbolo="Escorpion"
elif (mes==11 and dia>=22) or (mes==12 and dia<=21):
    simbolo="Sagitario"
elif (mes==12 and dia>=22) or (mes==1 and dia<=19):
    simbolo="Capricornio"
elif (mes==1 and dia>=20) or (mes==2 and dia<=18):
    simbolo="Acuario"
else:
    simbolo="Piscis"
print(simbolo)      