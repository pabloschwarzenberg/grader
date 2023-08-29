#Zodiaco
import datetime
dia = int(input("ingrese dia : "))
mes = int(input("ingrese mes : "))
ano = 2020
fecha = datetime.date(ano,mes,dia)
print("la fecha que ingreso es : ",fecha)
if datetime.date(ano,1,20)<=fecha<=datetime.date(ano,2,19):
    print("ACUARIO")
elif datetime.date(ano,2,19)<=fecha<=datetime.date(ano,3,21):
    print("PISCIS")
elif datetime.date(ano,3,21)<=fecha<=datetime.date(ano,4,20):
    print("ARIES")
elif datetime.date(ano,4,20)<=fecha<=datetime.date(ano,5,21):
    print("TAURO")
elif datetime.date(ano,5,21)<=fecha<=datetime.date(ano,6,21):
    print("GEMINIS")
elif datetime.date(ano,6,21)<=fecha<=datetime.date(ano,7,23):
    print("CANCER")
elif datetime.date(ano,7,23)<=fecha<=datetime.date(ano,8,23):
    print("LEO")
elif datetime.date(ano,8,23)<=fecha<=datetime.date(ano,9,23):
    print("VIRGO")
elif datetime.date(ano,9,23)<=fecha<=datetime.date(ano,10,23):
    print("LIBRA")
elif datetime.date(ano,10,23)<=fecha<=datetime.date(ano,11,22):
    print("ESCORPIO")
elif datetime.date(ano,11,22)<=fecha<=datetime.date(ano,12,22):
    print("SAGITARIO")
elif datetime.date(ano,12,22)<=fecha<=datetime.date(ano,1,20):
    print("CAPRICORNIO")
      