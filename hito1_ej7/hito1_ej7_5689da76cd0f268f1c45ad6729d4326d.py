dia= int(input("Ingresar dia de cumpleaños:   "))

mes= int(input("Ingresar mes de Cumpleaños:  "))

mesenero= 1
mesfebrero=2
mesmarzo=3
mesabril=4
mesmayo=5
mesjunio=6
mesjulio=7
mesagosto=8
messeptiembre=9
mesoctubre=10
mesnoviembre=11
mesdiciembre=12



if (dia) >= 21 and (mes) == 3 or (dia) <=19 and (mes) ==4:
    print("ARIES")
elif (dia) >=20 and (mes) == 4 or (dia) <= 20 and (mes)== 5:
    print ("TAURO")
elif (dia) >=21 and (mes) == 5 or (dia) <= 20 and (mes)== 6:
    print ("GEMINIS")
elif (dia) >=21 and (mes) == 6 or (dia) <= 22 and (mes)== 7:
    print ("CANCER")
elif (dia) >=23 and (mes) == 7 or (dia) <= 22 and (mes)== 8:
    print ("LEO")
elif (dia) >=23 and (mes) == 8 or (dia) <= 22 and (mes)== 9:
    print ("VIRGO")
elif (dia) >=23 and (mes) == 9 or (dia) <= 22 and (mes)== 10:
    print ("LIBRA")
elif (dia) >=23 and (mes) == 10 or (dia) <= 22 and (mes)== 11:
    print ("ESCORPION")
elif (dia) >=23 and (mes) == 11 or (dia) <= 21 and (mes)== 12:
    print ("SAGITARIO")
elif (dia) >=22 and (mes) == 12 or (dia) <= 19 and (mes)== 1:
    print ("CAPRICORNIO")
elif (dia) >=20 and (mes) == 1 or (dia) <= 18 and (mes)== 2:
    print ("ACUARIO")
elif (dia) >=19 and (mes) == 2 or (dia) <= 20 and (mes)== 3:
    print ("PISCIS")