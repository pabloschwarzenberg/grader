#Zodiaco
#HITO 1 - EJERCICIO 9: Signo del Zodíaco
# Para determinar las fechas de cada signo utiliza la columna
# Tropical Zodiac en la tabla de fechas que aparece en este link:

# LINK: en.wikipedia.org/wiki/Zodiac#Table_of_dates

dia = int(input('Ingresa el día de tu cumpleaños: '))
mes = int(input('Ingresa el mes de tu cumpleaños: '))

#ARIES: 21 Marzo – 20 Abril

#if naciste desde el 21 de marzo, hasta el 20 de abril:
    #imprimir 'ARIES' 

#dia :25
#mes: 3

if (dia>=21 and mes==3) or (dia<21 and mes==4):
    print("ARIES") 

#TAURO: 20 Abril – 21 Mayo

if (dia>=20 and mes==4) or (dia<22 and mes==5):
   print("TAURO")
   
#GEMINIS: 21 MAYO -21 JUNIO

if (dia>=21 and mes==5) or (dia<22 and mes==6):
    print("GEMINISIS")
    
#CANCER 21 JUNIO 23 JULIO

if (dia>=21 and mes==6) or (dia<24 and mes==7):
    print("CANCER")
    
#LEO 23 JULIO 23 AGOSTO

if (dia>=23 and mes==7) or (dia<24 and mes==8):
    print("LEO")
    
#VIRGO 23 AGOSTO 23 SEPTIEMBRE

if (dia>=23 and mes==7) or (dia<24 and mes==9):
    print("VIRGO")
    
#LIBRA 23 SEPTIEMBRE 23 OCTUBRE

if (dia>=23 and mes==9) or (dia<24 and mes==10):
    print("LIBRA")
    
#ESCORPIO 23 OCTUBRE 22 NOVIEMBRE

if (dia>=23 and mes==10) or (dia<23 and mes==11):
    print("ESCORPIO")
    
#SAGITARIO 22 NOVIEMBRE 22 DICIEMBRE

if (dia>=22 and mes==11) or (dia<23 and mes==12):
    print("SAGITARIO")
    
#CAPRICORNIO 22 DE DICIEMBRE AL 22 DE ENERO

if (dia>=22 and mes==12) or (dia<23 and mes==1):
    print("CAPRICORNIO")
    
#ACUARIO 20 ENERO 19 FEBRERO

if (dia>=20 and mes==1) or (dia<20 and mes==2):
    print("ACUARIO")
    
#PISCIS 19 FEBRERO 21 MARZO

if (dia>=19 and mes==2) or (dia<22 and mes==3):
    print("PISCIS")

