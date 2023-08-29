# Signos del Zodiaco

'''Signo
Aries	21 de marzo - 20 de abril
Tauro	21 de abril 20 de mayo
Géminis	21 de mayo - 21 de junio
Cáncer	22 de junio - 22 de julio
Leo	23 de julio - 23 de agosto
Virgo	24 de agosto - 23 de septiembre
Libra	24 de septiembre - 22 de octubre
Escorpio	23 de octubre - 22 de noviembre
Sagitario	23 de noviembre - 21 de diciembre
Capricornio	22 de diciembre - 19 de enero
Acuario	20 de enero - 19 de febrero
Piscis	20 de febrero - 20 de marzo
'''

#anio = int(input("Ingrese su año de nacimiento: "))
dia = int(input("Ingrese su día de nacimiento: "))
mes = input("Ingrese su mes de nacimiento:" )


if (mes=='3' or mes=='4'):
    if (dia>=1 and dia<=21):
        print("Aries ")
    elif (dia>=22 and dia<=30):
        print("Tauro")
elif (mes=='5'):
    if (dia>=1 and dia<=20):
        print("Tauro")
    elif (dia>=21 and dia<=31):
        print("Géminis")
elif (mes=='6'):
    if (dia>=1 and dia<=21):
        print("Géminis")
    elif(dia>21 and dia <=30):
        print("Cáncer")
elif (mes=='7'):
    if (dia>=1 and dia <=22):
        print("Cáncer")
    elif (dia>22 and dia <=31):
        print("Leo")
elif (mes=='8'):
    if (dia>=1 and dia <=23):
        print("Leo")
    elif (dia>23 and dia <=31):
        print("Virgo")
elif (mes=='9'):
    if (dia>=1 and dia <=23):
        print("Virgo")
    elif(dia>23 and dia <=30):
        print("Libra")
elif (mes =='10'):
    if (dia>=1 and dia <=23):
        print("Libra")
    elif(dia>23 and dia <=31):
        print("Escorpio")
elif (mes=='11'):
    if (dia>=1 and dia <=22):
        print("Escorpio")
    elif(dia>22 and dia <=30):
        print("Sagitario")
elif (mes=='12'):
    if (dia>=1 and dia <=23):
        print("Sagitario")
    elif(dia>23 and dia <=31):
        print("Capricornio")
elif (mes=='1'):
    if (dia>=1 and dia <=19):
        print("Capricornio")
    elif(dia>23 and dia <=31):
        print("Acuario")
elif (mes=='2'):
    if (dia>=1 and dia <=19):
        print("Acuario")
    elif(dia>19 and dia <=29):
        print("Piscis")
else:
    print("Por favor, revise sus datos e intente de nuevo") 