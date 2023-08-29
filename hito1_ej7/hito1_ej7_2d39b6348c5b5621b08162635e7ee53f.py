dia = int(input("ingrese el dia de su cumpleaños"))
mes = int(input("ingrese el mes de su cumpleaños"))

signo = ("capricornio", "acuario", "piscis", "aries", "tauro", "géminis", "cáncer", "leo", "virgo", "libra", "escorpio", "sagitario")
fechas = (20, 19, 20, 20, 21, 21, 22, 22, 22, 22, 22, 21)
if dia<= 21 and mes==3 or mes==4:
    print("aries")
elif dia<= 21 and mes==4 or mes == 5:
    print("Tauro")
elif dia>=21 and mes==5 or mes==6:
    print("Geminis")
elif dia<=23 and mes==6 or mes==7:
    print("Cancer")
elif dia <= 23 and mes==7 or mes==8:
    print("Leo")
elif dia<= 23 and mes== 8 or mes==9:
    print("virgo")
elif dia <=23 and mes==9 or mes==10:
    print("Libra")
elif dia <=23 and mes== 10 or mes==11:
    print("Escorpion")
elif dia <= 23 and mes == 11 or mes==12:
    print("sagitario")
elif dia <= 22 and mes== 12 or mes==1:
    print("Capricornio")
elif dia <= 20 and mes== 1 or mes==2:
    print("Acuario")
elif dia <=21 and mes== 2 or mes==3:
    print("Piscis")
else:
    print("numeros no validos")     