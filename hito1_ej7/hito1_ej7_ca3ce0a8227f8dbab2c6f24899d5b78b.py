#Zodiaco
import datetime
dia = int(input("ingrese el dia: "))
mes = int(input("ingrese el mes: "))
aaaa = 2020
fecha = datetime.date(aaaa,mes,dia)
if datetime.date(aaaa,1,20)<=fecha<=datetime.date(aaaa,2,19):
  print("Acuario")
if datetime.date(aaaa,2,19)<=fecha<=datetime.date(aaaa,3,21):
  print("Piscis")
if datetime.date(aaaa,3,21)<=fecha<=datetime.date(aaaa,4,20):
  print("Aries")
if datetime.date(aaaa,4,20)<=fecha<=datetime.date(aaaa,5,21):
  print("Tauro")
if datetime.date(aaaa,5,21)<=fecha<=datetime.date(aaaa,6,21):
  print("Geminis")
if datetime.date(aaaa,6,21)<=fecha<=datetime.date(aaaa,7,23):
  print("Cancer")
if datetime.date(aaaa,7,23)<=fecha<=datetime.date(aaaa,8,23):
  print("Leo")
if datetime.date(aaaa,8,23)<=fecha<=datetime.date(aaaa,9,23):
  print("Virgo")
if datetime.date(aaaa,9,23)<=fecha<=datetime.date(aaaa,10,23):
  print("Libra")
if datetime.date(aaaa,10,23)<=fecha<=datetime.date(aaaa,11,22):
  print("Escorpion")
if datetime.date(aaaa,11,22)<=fecha<=datetime.date(aaaa,12,22):
  print("Sagitario")
else:
    print("Capricornio")
