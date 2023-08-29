#Zodiaco
Enero=1
Febrero=2
Marzo=3
Abril=4
Mayo=5
Junio=6
Julio=7
Agosto=8
Septiembre=9
Octubre=10
Noviembre=11
Diciembre=12
Dia=int(input("Ingrese Dia de Cumpleaños:"))
Mes=int(input("Ingrese Mes de Cumpleaños:"))
if (Mes==1 and Dia<=21):
    print("Capricornio")
elif(Mes==1 and Dia>21):
    print("Acuario")
###########################
elif(Mes==2 and Dia<=18):
    print("Acuario")
elif (Mes==2 and Dia>18):
    print("Piscis")
###########################
elif(Mes==3 and Dia<=23):
    print("Piscis")
elif(Mes==3 and Dia>23):
    print("Aries")
##########################
elif(Mes==4 and Dia<=21):
    print("Aries")
elif(Mes==4 and Dia>21):
    print("Taurus")
##########################
elif (Mes==5 and Dia<=21):
    print("Taurus")
elif(Mes==5 and Dia>21):
    print("Geminis")
##########################
elif (Mes==6 and Dia<=21):
    print("Geminis")
elif(Mes==6 and Dia>21):
    print("Cancer")
##########################
elif (Mes==7 and Dia<=21):
    print("Cancer")
elif(Mes==7 and Dia>21):
    print("Leo")
##########################
elif (Mes==8 and Dia<=23):
    print("Leo")
elif(Mes==8 and Dia>23):
    print("Virgo")
##########################
elif (Mes==9 and Dia<=21):
    print("Virgo")
elif(Mes==9 and Dia>21):
    print("Libra")
##########################
elif (Mes==10 and Dia<=21):
    print("Libra")
elif(Mes==10 and Dia>21):
    print("Escorpion")
###########################
elif (Mes==11 and Dia<=22):
    print("Escorpion")
elif(Mes==11 and Dia>22):
    print("Sagitario")
###########################
elif (Mes==12 and Dia<=21):
    print("Sagitario")
elif(Mes==12 and Dia>21):
    print("Capricornio")
else:
    print("Error")