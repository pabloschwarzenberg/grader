#Zodiaco
from datetime import date
dia=int(input("Ingresar día de nacimiento: "))
mes=int(input("Ingresar mes de nacimiento: "))
a=2020
fecha=date(a, mes, dia)
if date(a,1,21)<=fecha<=date(a,2,19):
    print("acuario")
elif date(a,2,20)<=fecha<=date(a,3,20):
    print("piscis")
elif date(a,3,21)<=fecha<=date(a,4,20):
    print("aries")
elif date(a,4,21)<=fecha<=date(a,5,21):
    print("tauro")
elif date(a,5,22)<=fecha<=date(a,6,21):
    print("geminis")
elif date(a,6,22)<=fecha<=date(a,7,22):
    print("cancer")
elif date(a,7,23)<=fecha<=date(a,8,23):
    print("leo")
elif date(a,8,24)<=fecha<=date(a,9,23):
    print("virgo")
elif date(a,9,24)<=fecha<=date(a,10,23):
    print("libra")
elif date(a,10,24)<=fecha<=date(a,11,22):
    print("escorpion")
elif date(a,11,23)<=fecha<=date(a,12,21):
    print("sagitario")
else:
    print("capricornio")