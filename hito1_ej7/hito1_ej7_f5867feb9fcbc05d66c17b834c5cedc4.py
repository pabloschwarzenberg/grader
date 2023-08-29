#ENTRADA
dia = int(input("Ingrese su día de nacimiento: "))
mes = input("Ingrese su mes de nacimiento:" )

#PROCESAMIENTO Y SALIDA
#MARZO
if (mes=='3' or mes=='4'):
    if (dia>=1 and dia<=21):
        print("Signo: Aries")
    elif (dia>=22 and dia<=30):
        print("Signo: Tauro")

#MAYO
elif (mes=='5'):
    if (dia>=1 and dia<=20):
        print("Signo: Tauro")
    elif (dia>=21 and dia<=31):
        print("Signo: Géminis")

#JUNIO
elif (mes=='6'):
    if (dia>=1 and dia<=21):
        print("Signo: Géminis")
    elif(dia>21 and dia <=30):
        print("Signo: Cáncer")

#JULIO
elif (mes=='7'):
    if (dia>=1 and dia <=22):
        print("Signo: Cáncer")
    elif (dia>22 and dia <=31):
        print("Signo: Leo")

#AGOSTO
elif (mes=='8'):
    if (dia>=1 and dia <=23):
        print("Signo: Leo")
    elif (dia>23 and dia <=31):
        print("Signo: Virgo")

#SEPTIEMBRE
elif (mes=='9'):
    if (dia>=1 and dia <=23):
        print("Signo: Virgo")
    elif(dia>23 and dia <=30):
        print("Signo: Libra")

#OCTUBRE
elif (mes =='10'):
    if (dia>=1 and dia <=23):
        print("Signo: Libra")
    elif(dia>23 and dia <=31):
        print("Signo: Escorpio")

#NOVIEMBRE
elif (mes=='11'):
    if (dia>=1 and dia <=22):
        print("Signo: Escorpio")
    elif(dia>22 and dia <=30):
        print("Signo: Sagitario")

#DICIEMBRE
elif (mes=='12'):
    if (dia>=1 and dia <=23):
        print("Signo: Sagitario")
    elif(dia>23 and dia <=31):
        print("Signo: Capricornio")

#ENERO
elif (mes=='1'):
    if (dia>=1 and dia <=19):
        print("Signo: Capricornio")
    elif(dia>23 and dia <=31):
        print("Signo: Acuario")

#FEBRERO
elif (mes=='2'):
    if (dia>=1 and dia <=19):
        print("Signo: Acuario")
    elif(dia>19 and dia <=29):
        print("Signo: Piscis")

#DATOS INCORRECTOS
else:
    print("Por favor, revise sus datos e intente de nuevo")