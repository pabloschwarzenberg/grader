#Zodiaco
dia = eval(input("ingrese el dia de su cumpleaños: "))
mes = eval(input("El mes de cumpleaños "))

if dia>=21 and mes ==3 or dia<=20 and mes == 4:
  print("aries")
if dia>=21 and mes ==4 or dia<=21 and mes == 5:
  print("Tauro")
if dia>21 and mes==5 or dia<=21 and mes == 6:
  print("Geminis")
if dia>21 and mes ==6 or dia<=23 and mes == 7:
  print("Cancer")
if dia>24 and mes == 7 or dia<=23 and mes == 8:
  print("Leon")
if dia>23 and mes == 7 or dia<=23 and mes ==9:
  print("Virgo")
if dia>23 and mes == 9 or dia<=23 and mes == 10:
  print("Libra")
if dia>23 and mes == 10 or dia<=22 and mes == 11:
  print("Escorpion")
if dia>22 and mes == 11 or dia<=22 and mes ==12:
  print("Sagitario")
if dia>22 and mes == 12 or dia<=20 and mes == 1:
  print("Capricornio")
if dia>20 and mes == 1 or dia<=19 and mes == 2:
  print("Acuario")
if dia>19 and mes == 2 or dia<21 and mes == 3:
  print("Piscis")

