#Zodiaco
mes = 0
dia = 0
Aries = 0
Geminis = 0
Cancer = 0
leo = 0
Virgo = 0
Escorpion = 0
Sagitario = 0
Capricornio = 0
Acuario = 0
Piscis = 0

dia=int(input("En que dia naciste: "))
mes=int(input("En que mes naciste: "))


if ((mes == 3 and dia >= 22 ) or (mes == 4 and dia <= 20)):
    print("Aries")
elif ((mes == 4 and dia >= 21 ) or (mes == 5 and dia <= 21)):
    print("Tauro")
elif ((mes == 5 and dia >= 22 ) or (mes == 6 and dia <= 21)):
    print("Geminis")
elif ((mes == 6 and dia >= 22) or (mes == 7 and dia <= 23)):
    print("Cancer")
elif ((mes == 7 and dia >=24) or (mes == 8 and dia <= 23)):
    print("Leo")
elif ((mes == 8 and dia >=24) or (mes == 9 and dia <= 23)):
    print("Virgo")
elif ((mes == 9 and dia >= 24) or (mes == 10 and dia <= 23)):
    print("Libra")
elif ((mes == 10 and dia >=24) or (mes == 11 and dia <= 22)):
    print("Escorpion")
elif ((mes == 11 and dia >=23) or (mes == 12 and dia <= 23)):
    print("Sagitario")
elif ((mes == 12 and dia >=23) or (mes == 1 and dia <= 20)):
    print("Capricornion")
elif ((mes == 1 and dia >=21) or (mes == 2 and dia <= 19)):
    print("Acuario")
else:
    print("Piscis")     