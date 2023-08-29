#Zodiaco
dia=int(input("En que dia naciste: "))
mes=int(input("En que mes naciste: "))

if ((mes == 3 and dia >= 22 ) or (mes == 4 and dia <= 20)):
    print("Aries")
elif ((mes == 4 and dia >= 21 ) or (mes == 5 and dia <= 21)):
    print("Tauro")
elif ((mes == 5 and dia >= 22 ) or (mes == 6 and dia <= 21)):
    print("geminis")
elif ((mes == 6 and dia >= 22) or (mes == 7 and dia <= 23)):
    print("cancer")
elif ((mes == 7 and dia >=24) or (mes == 8 and dia <= 23)):
    print("leo")
elif ((mes == 8 and dia >=24) or (mes == 9 and dia <= 23)):
    print("virgo")
elif ((mes == 9 and dia >= 24) or (mes == 10 and dia <= 23)):
    print("libra")
elif ((mes == 10 and dia >=24) or (mes == 11 and dia <= 22)):
    print("scorpio")
elif ((mes == 11 and dia >=23) or (mes == 12 and dia <= 23)):
    print("sagitario")
elif ((mes == 12 and dia >=23) or (mes == 1 and dia <= 20)):
    print("capricornio")
elif ((mes == 1 and dia >=21) or (mes == 2 and dia <= 19)):
    print("acuario")
else:
    print("piscis")