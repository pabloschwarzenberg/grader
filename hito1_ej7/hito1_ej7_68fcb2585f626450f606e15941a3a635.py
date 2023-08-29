#Zodiaco
import datetime
dia=int(input("ingrese dia"))
mes=int(input("ingrese mes"))
aaaa=2020
fecha=datetime.date(aaaa,mes,dia)
print("la fecha que ingreso es",fecha)
if datetime.date(aaaa,1,20)<=fecha<=datetime.date(aaaa,2,19):
    print("acuario")
elif datetime.date(aaaa,2,19)<=fecha<=datetime.date(aaaa,3,21):
    print("Piscis")
elif datetime.date(aaaa,3,21)<=fecha<=datetime.date(aaaa,4,20):
    print("Aries")
elif datetime.date(aaaa,4,20)<=fecha<=datetime.date(aaaa,5,21):
    print("Tauro")
elif datetime.date(aaaa,5,21)<=fecha<=datetime.date(aaaa,6,21):
    print("Geminis")
elif datetime.date(aaaa,6,21)<=fecha<=datetime.date(aaaa,7,23):
    print("Cancer")
elif datetime.date(aaaa,7,23)<=fecha<=datetime.date(aaaa,8,23):
    print("Leo")
elif datetime.date(aaaa,8,23)<=fecha<=datetime.date(aaaa,9,23):
    print("Virgo")
elif datetime.date(aaaa,9,23)<=fecha<=datetime.date(aaaa,10,23):
    print("Libra")
elif datetime.date(aaaa,10,23)<=fecha<=datetime.date(aaaa,11,22):
    print("Escorpio")
elif datetime.date(aaaa,11,22)<=fecha<=datetime.date(aaaa,12,22):
    print("Sagitario")
elif datetime.date(aaaa,12,22)<=fecha or fecha<=datetime.date(aaaa,1,20):
    print("Capricornio")
              