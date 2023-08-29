#Zodiaco
import datetime
dia = int(input("Ingrese día: "))
mes = int(input("Ingrese mes: "))
ano = 2020
fecha = datetime.date(ano,mes,dia)
if datetime.date(2020,3,21)<=fecha<=datetime.date(2020,4,20):
    print("aries")
elif datetime.date(2020,4,20)<=fecha<=datetime.date(2020,5,21):
    print("tauro")
elif datetime.date(2020,5,21)<=fecha<=datetime.date(2020,6,21):
    print("geminis")
elif datetime.date(2020,6,21)<=fecha<=datetime.date(2020,7,23):
    print("cancer")
elif datetime.date(2020,7,23)<=fecha<=datetime.date(2020,8,23):
    print("leo")
elif datetime.date(2020,8,23)<=fecha<=datetime.date(2020,9,23):
    print("virgo")
elif datetime.date(2020,9,23)<=fecha<=datetime.date(2020,10,23):
    print("libra")
elif datetime.date(2020,10,23)<=fecha<=datetime.date(2020,11,22):
    print("escorpion")
elif datetime.date(2020,11,22)<=fecha<=datetime.date(2020,12,22):
    print("sagitario")
elif datetime.date(2020,12,22)<=fecha<=datetime.date(2020,1,20):
    print("capricornio")
elif datetime.date(2020,1,20)<=fecha<=datetime.date(2020,2,19):
    print("acuario")
elif datetime.date(2020,2,19)<=fecha<=datetime.date(2020,3,21):
    print("piscis")