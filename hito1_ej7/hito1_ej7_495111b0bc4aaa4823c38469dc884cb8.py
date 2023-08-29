#Zodiaco
dia = int(input("Ingrese día de cumpleaños: "))
mes = int(input("Ingrese mes de cumpleaños, con numeros: "))
if (mes == 3) and (31 >= dia >= 21) or (mes == 4) and (19 >= dia >= 1):
    print("Signo del zodíaco: Aries")
elif (mes == 4) and (30 >= dia >= 20) or (mes == 5) and (20 >= dia >= 1):
    print("Signo del zodíaco: Tauro")
elif (mes == 5) and (31 >= dia >= 21) or (mes == 6) and (20 >= dia >= 1):
    print("Signo del zodíaco: Geminis")
elif (mes == 6) and (30 >= dia >= 21) or (mes == 7) and (22 >= dia >= 1):
    print("Signo del zodíaco: Cancer")
elif (mes == 7) and (31 >= dia >= 23) or (mes == 8) and (22 >= dia >= 1):
    print("Signo del zodíaco: Leo")
elif (mes == 8) and (31 >= dia >= 23) or (mes == 9) and (22 >= dia >= 1):
    print("Signo del zodíaco: Virgo")
elif (mes == 9) and (30 >= dia >= 23) or (mes == 10) and (22 >= dia >= 1):
    print("Signo del zodíaco: Libra")
elif (mes == 10) and (31 >= dia >= 23) or (mes == 11) and (21 >= dia >= 1):
    print("Signo del zodíaco: Escorpio")
elif (mes == 11) and (30 >= dia >= 22) or (mes == 12) and (21 >= dia >= 1):
    print("Signo del zodíaco: Sagitario")
elif (mes == 12) and (31 >= dia >= 22) or (mes == 1) and (21 >= dia >= 1):
    print("Signo del zodíaco: Capricornio")
elif (mes == 1) and (31 >= dia >= 22) or (mes == 2) and (18 >= dia >= 1):
    print("Signo del zodíaco: Acuario")
elif (mes == 2) and (29 >= dia >= 19) or (mes == 3) and (20 >= dia >= 1):
    print("Signo del zodíaco: Piscis")      