#Zodiaco
dia = int(input("Escribe el dia: " ))
mes = int(input("Escribe el mes: " ))

if ((mes == 3) and (dia >= 21)) or ((mes == 4) and (dia <= 20)):
    print("Signo = Aries")

elif ((mes == 4) and (dia >= 20)) or ((mes == 5) and (dia <= 21)):
    print("Signo = Tauro")

elif ((mes == 5) and (dia >= 21)) or ((mes == 6) and (dia <= 21)):
    print("Signo = Geminis")

elif ((mes == 6) and (dia >= 21)) or ((mes == 7) and (dia <= 23)):
    print("Signo = Cancer")

elif ((mes == 7) and (dia >= 23)) or ((mes == 8) and (dia <= 23)):
    print("Signo = Leo")

elif ((mes == 8) and (dia >= 23)) or ((mes == 9) and (dia <= 23)):
    print("Signo = Virgo")

elif ((mes == 9) and (dia >= 23)) or ((mes == 10) and (dia <= 23)):
    print("Signo = Libra")

elif ((mes == 10) and (dia >= 23)) or ((mes == 11) and (dia <= 22)):
    print("Signo = Escorpion")

elif ((mes ==11) and (dia >= 22)) or ((mes == 12) and (dia <= 22)):
    print("Signo = Sagitario")

elif ((mes == 12) and (dia >= 22)) or ((mes == 1) and (dia <= 20)):
    print("Signo = Capricornio")

elif ((mes == 1) and (dia >= 20)) or ((mes == 2) and (dia <= 19)):
    print("Signo = Aquario")

elif ((mes == 2) and (dia >= 19)) or ((mes == 3) and (dia <= 21)):
    print("Signo = Piscis")     