#Signo del Zodiaco


print("***Signo del zodiaco a partir de la fecha de cumpleaño***")

while True:
    dia=int(input("Ingrese el dia:"))
    if(dia>31 or dia<1):
        print("Dia invalido, vuelva a intentarlo")
    else:
        break
while True:
    mes=int(input("ingrese el mes:"))
    if(mes>12 or mes<1):
        print("mes invalido, vuelve a intentarlo")
    else:
        break
    
if(mes>=1 and mes<12):
    if(mes==3 and dia>=21):
        print("Usted es Aries")
    elif(mes==4 and dia<=20):
        print("Usted es Aries")
    elif(mes==4 and dia>=21):
        print("Usted es Tauro")
    elif(mes==5 and dia<=20):
        print("Usted es Tauro")     
    elif(mes==5 and dia<=21):
        print("Usted es Gemenis")
    elif(mes==6 and dia<=20):
        print("Usted es Gemenis")
    elif(mes==6 and dia>=21):
         print("Usted es Cancer")
    elif(mes==7 and dia<=22):
         print("Usted es Cancer")
    elif(mes==7 and dia>=23):
         print("Usted es Leo")
    elif(mes==8 and dia<=22):
         print("Usted es Leo")
    elif(mes==8 and dia>=23):
         print("Usted es Virgo")
    elif(mes==9 and dia<=22):
         print("Usted es Virgo")
    elif(mes==9 and dia>=23):
         print("Usted es Libra")
    elif(mes==10 and dia<=22):
         print("Usted es Libra")
    elif(mes==10 and dia>=23):
         print("Usted es Escorpion")
    elif(mes==11 and dia<=21):
         print("Usted es Escorpion")
    elif(mes==11 and dia>=22):
         print("Usted es Sagitario")
    elif(mes==12 and dia<=21):
         print("Usted es Sagitario")
    elif(mes==12 and dia>=22):
         print("Usted es Capricornio")
    elif(mes==1 and dia<=19):
         print("Usted es Capricornio")
    elif(mes==1 and dia>=20):
         print("Usted es Acuario")
    elif(mes==2 and dia<=18):
         print("Usted es Acuario")
    elif(mes==2 and dia>=19):
         print("Usted es Piscis")
    elif(mes==3 and dia<=20):
         print("Usted es Piscis")
