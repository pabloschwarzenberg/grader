#Zodiaco
import datetime
dia = int(input("ingrese dia: "))
mes = int(input("ingrese mes: "))
aaa = 2020
fecha = datetime.date(aaa,mes,dia)
print("la fecha que ingreso es: ",fecha)
if datetime.date(aaa,1,20)<=fecha<=datetime.date(aaa,2,19):
    print("acuario")
elif datetime.date(aaa,2,19)<=fecha<=datetime.date(aaa,3,21):
    print("piscis")
elif datetime.date(aaa,3,21)<=fecha<=datetime.date(aaa,4,20):
    print("aries")
elif datetime.date(aaa,4,20)<=fecha<=datetime.date(aaa,5,21):
    print("tauro")
elif datetime.date(aaa,5,21)<=fecha<=datetime.date(aaa,6,21):
    print("geminis")
elif datetime.date(aaa,6,21)<=fecha<=datetime.date(aaa,7,23):
    print("cancer")
elif datetime.date(aaa,7,23)<=fecha<=datetime.date(aaa,8,23):
    print("leo")
elif datetime.date(aaa,8,23)<=fecha<=datetime.date(aaa,9,23):
    print("virgo")
elif datetime.date(aaa,9,23)<=fecha<=datetime.date(aaa,10,23):
    print("libra")
elif datetime.date(aaa,10,23)<=fecha<=datetime.date(aaa,11,22):
    print("escorpion")
elif datetime.date(aaa,11,22)<=fecha<=datetime.date(aaa,12,22):
    print("sagitario")
elif datetime.date(aaa,12,22)<=fecha<=datetime.date(aaa,1,20):
    print("capricornio")
      