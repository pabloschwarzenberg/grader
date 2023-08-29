#entrada:reciba 2 numeros enteros que representaran el dia y el mes
#salida:muestre a que signo zodiacal pertenece
#los numeros son:
dia=int(input("el dia es: "))
while not(dia>0 and dia<32):
    dia=int(input("error, el dia del calendario puede ser del 1 al 31: "))
mes=int(input("el mes es: "))
while not(mes>0 and mes<13):
    mes=int(input("error, el mes debe estar entre 1 y 12: "))
#dependiendo de las fechas, identificar el signo zodiacal:
if ((dia>=21 and dia<=31 and mes==3)or(dia>=1 and dia<=20 and mes==4)):
    print("Aries")
elif((dia>=20 and dia<=30 and mes==4)or(dia>=1 and dia<=21 and mes==5)):
    print("Tauro")
elif((dia>=21 and dia<=31 and mes==5)or(dia>=1 and dia<=21 and mes==6)):
    print("Géminis")
elif((dia>=21 and dia<=30 and mes==6)or(dia>=1 and dia<=23 and mes==7)):
    print("Cáncer")
elif((dia>=23 and dia<=31 and mes==7)or(dia>=1 and dia<=23 and mes==8)):
    print("León")
elif((dia>=23 and dia<=31 and mes==8)or(dia>=1 and dia<=23 and mes==9)):
    print("Virgo")
elif((dia>=23 and dia<=30 and mes==9)or(dia>=1 and dia<=23 and mes==10)):
    print("Libra")
elif((dia>=23 and dia<=31 and mes==10)or(dia>=1 and dia<=22 and mes==11)):
    print("Escorpión")
elif((dia>=23 and dia<=30 and mes==11)or(dia>=1 and dia<=22 and mes==12)):
    print("Sagitario")
elif((dia>=22 and dia<=31 and mes==12)or(dia>=1 and dia<=20 and mes==1)):
    print("Capricornio")
elif((dia>=20 and dia<=31 and mes==1)or(dia>=1 and dia<=19 and mes==2)):
    print("Acuario")
elif((dia>=19 and dia<=29 and mes==2)or(dia>=1 and dia<=21 and mes==3)):
    print("Piscis")
