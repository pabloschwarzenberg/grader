#Zodiaco
#Cálculo del dígito verificador de un rut
dia_del_cumpleaños = int(input("dia de cumpleaños: "))
mes_del_cumpleaños = int(input("mes de cumpleaños: "))
#poner los signos segun el mes y dia 
# Ordenar los meses segun su signo
if mes_del_cumpleaños == 1:
    if dia_del_cumpleaños >=1 and dia_del_cumpleaños < 21:
        print("Capricornio")
    else:
        print("Acuario")
if mes_del_cumpleaños == 2:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños < 19:
        print("Acuario")
    else:
        print("piscis")
if mes_del_cumpleaños == 3:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños < 21:
        print("piscis")
    else:
        print("Aries")
if mes_del_cumpleaños == 4:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños < 22:
        print("Aries")
    else: 
         print("Tauro")
if mes_del_cumpleaños == 5:
    if dia_del_cumpleaños>= 1 and dia_del_cumpleaños < 22:
        print("Tauro")
    else:
        print("Geminis")
if mes_del_cumpleaños == 6:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños < 23:
        print("Geminis")
    else:
        print("Cancer")
if mes_del_cumpleaños == 7:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños < 24:
        print("Cancer")
    else:
        print("Leo")
if mes_del_cumpleaños == 8:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños < 24:
        print("Leo")
    else:
        print("Virgo")
if mes_del_cumpleaños == 9:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños < 24:
        print("Virgo")
    else:
        print("Libra")
if mes_del_cumpleaños == 10:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños < 24:
        print("Libra")
    else:
        print("Escorpion")
if mes_del_cumpleaños == 11:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños< 23:
        print("Escorpion")
    else:
        print("Sagitario")
if mes_del_cumpleaños == 12:
    if dia_del_cumpleaños >= 1 and dia_del_cumpleaños < 22:
        print("Sagitario")
    else:
        print("Capricornio")