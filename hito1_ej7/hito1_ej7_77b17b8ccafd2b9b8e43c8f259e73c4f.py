'''

Escribe un programa que reciba como parámetro el día y el mes del cumpleaños de una persona (como números enteros) y que imprima el signo 
del zodíaco al que pertenece.

Para determinar las fechas de cada signo utiliza la columna Tropical Zodiac en la tabla de fechas que aparece en este link (Wikipedia).
'''

dia = int(input("ingrese el dia del cumpleaños: "))
mes = int(input("ingrese el mes de su cumpleaños: "))

signo = ""
if( mes == 3):
    if(dia >= 21):
        signo = "Aries"
    else:
        signo = "Picis"
elif( mes == 4):
    if(dia >= 20):
        signo = "Tauro"
    else:
        signo = "Aries"
elif( mes == 5):
    if(dia >= 21):
        signo = "Geminis"
    else:
        signo = "Tauro"
elif( mes == 6):
    if( dia >= 21):
        signo = "Cancer"
    else:
        signo = "Gemenis"
elif( mes == 7):
    if(dia >= 23):
        signo = "Leo"
    else:
        signo = "Cancer"
elif( mes == 8):
    if(dia>= 23):
        signo = "Virgo"
    else:
        signo = "Leo"
elif( mes == 9):
    if(dia >= 23):
        signo = "Libra"
    else:
        signo = "Virgo"
elif( mes == 10):
    if(dia >= 23):
        signo = "Escorpion"
    else:
        signo = "Libra"
elif( mes == 11):
    if(dia >= 23):
        signo = "Sagitario"
    else:
        signo = "Escorpion"
elif( mes == 12):
    if( dia >= 22):
        signo = "Capricornio"
    else:
        signo = "Sagitario"
elif( mes == 1):
    if( dia >=20):
        signo = "Acuario"
    else:
        signo = "Capricornio"
elif(mes == 2):
    if( dia >= 19):
        signo = "Picis"
    else:
        signo = "Acuario"


print(signo)