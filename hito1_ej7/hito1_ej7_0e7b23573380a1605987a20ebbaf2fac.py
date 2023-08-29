#Zodiaco
dia=int(input("Ingrese el dia de cumpleaños: "))
mes=int(input(("Ingrese el mes de cumpleaños: ")))
if 31 >= dia >= 21 and mes == 3 or 19 >= dia >=1 and mes == 4:
    print("Aries")
elif 30 >= dia >= 20 and mes == 4 or 20 >= dia >= 1 and mes == 5:
    print("Tauro")
elif 31 >= dia >= 21 and mes == 5 or 20 >= dia >= 1 and mes == 6:
    print("Géminis")
elif 30 >= dia >= 21 and mes == 6 or 22 >= dia >= 1 and mes == 7:
    print("Cancer")
elif 31 >= dia >= 23 and mes== 7 or 22 >= dia >= 1 and mes == 8:
    print("Leo")
elif 31 >= dia >= 23 and mes == 8 or 22 >= dia >= 1 and mes == 9:
    print("Virgo")
elif 31 >= dia >= 23 and mes == 9 or 22 >= dia >= 1 and mes == 10:
    print("Libra")
elif 31 >= dia >= 23 and mes == 10 or 21 >= dia >= 1 and mes == 11:
    print("Escorpio")
elif 30 >= dia >= 22 and mes == 11 or 21 >= dia >= 1 and mes == 12:
    print("Sagitario")
elif 31 >= dia >= 22 and mes == 12 or 19>= dia >= 1 and mes == 1:
    print("Capricornio")
elif 31 >= dia >= 20 and mes == 1 or 18 >= dia >= 1 and mes == 2:
    print("Acuario")
elif 28 >= dia >= 19 and mes == 2 or 20 >= dia >= 1 and mes == 3:
    print("Piscis")