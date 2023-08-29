Dia = eval(input("ingrese el dia:"))
Mes = str(input("ingrese el mes:"))


if (Dia >= 20) and (Dia <= 31) and (Mes=="1") or (Dia>=1) and (Dia<19) and (Mes=="2"):
    print ("Acuario")

elif (Dia >= 19) and (Dia <= 30) and (Mes=="2") or (Dia>=1) and (Dia < 21) and (Mes=="3"):
    print ("Piscis")

elif (Dia >= 21) and (Dia <= 31) and (Mes=="3") or (Dia>=1) and (Dia < 20) and (Mes=="4"):
    print ("Aries")

elif (Dia >= 20) and (Dia <= 31) and (Mes=="4")or (Dia>=1) and (Dia < 21) and (Mes=="5"):
    print ("Tauro")

elif (Dia >= 21) and (Dia <= 31) and (Mes=="5") or (Dia>=1) and (Dia < 21) and (Mes=="6"):
    print ("Geminis")

elif (Dia >= 21) and (Dia <= 31) and (Mes=="6") or (Dia>=1) and (Dia < 23) and (Mes=="7"):
    print ("Cancer")

elif (Dia >= 23) and (Dia <= 31) and (Mes=="7") or (Dia>=1) and (Dia < 23) and (Mes=="8"):
    print ("Leo")

elif (Dia >=23 ) and (Dia <= 31) and (Mes=="8") or (Dia>=1) and (Dia < 23) and (Mes=="9"):
    print ("Virgo")

elif (Dia >= 23) and (Dia <= 31) and (Mes=="9") or (Dia>=1) and (Dia < 23) and (Mes=="10"):
    print ("Libra")

elif (Dia >= 23) and (Dia <= 31) and (Mes=="10") or (Dia>=1) and (Dia < 22) and (Mes=="11"):
    print ("Escorpio")

elif (Dia >= 22) and (Dia <= 31) and (Mes=="11") or (Dia>=1) and (Dia < 22) and (Mes=="12"):
    print ("Sagitario")

elif (Dia >= 22) and (Dia <= 31) and (Mes=="12") or (Dia>=1) and (Dia < 20) and (Mes=="1"):
    print ("Capricornio")

else :
    print ("No es posible")