#Escribe un programa que reciba como parámetro el día y el mes del cumpleaños de una persona (como números enteros) y que imprima el signo del zodíaco al que pertenece.
from os import system
system ("cls")
dia = int(input("Ingrese su dia de nacimiento (1-31): "))
mes = int(input("Ingrese su mes de nacimiento [1] Enero     [2] Febrero     \n[3] Marzo     [4] Abril     \n[5] Mayo     [6] Junio     \n[7] Julio     [8] Agosto     \n[9] Septiembre     [10] Octubre     \n[11] Noviembre     [12] Diciembre\n:"))

if dia <= 1 and dia >= 21 and mes >=3 or mes <=4:
    print("Aries")

if dia <= 1 and dia >= 21 and mes >=4 or mes <=5:
    print("Tauro")

if dia <= 1 and dia >= 22 and mes >=5 or mes <=6:
    print("Geminis")

if dia <= 1 and dia >= 23 and mes >=6 or mes <=7:
    print("Gancer")

if dia <= 1 and dia >= 24 and mes >=7 or mes <=8:
    print("Leo")

if dia <= 1 and dia >= 24 and mes >=8 or mes <=9:
    print("Virgo")

if dia <= 1 and dia >= 24 and mes >=9 or mes <=10:
    print("Libra")

if dia <= 1 and dia >= 24 and mes >=10 or mes <=11:
    print("Escorpio")

if dia <= 1 and dia >= 23 and mes >=11 or mes <=12:
    print("Sagitario")

if dia <= 1 and dia >= 22 and mes >=12 or mes <=1:
    print("Capricornio")

if dia <= 1 and dia >= 21 and mes >=1 or mes <=2:
    print("Acuario")

if dia <= 1 and dia >= 20 and mes >=2 or mes <=3:
    print("Piscis")