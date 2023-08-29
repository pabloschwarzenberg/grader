#Aprobación de créditos
ingreso = int(input(" Introduzca su ingreso en pesos : "))
nacimiento = int(input(" introduzca su año de nacimiento :"))
hijos = int(input(" Introduzco la cantidad de hijos que tiene :"))
añosbanco = int(input(" Introduzca la cantidad de años que pertenece al banco :"))
estado_c = input(" Introduzca su estado civil (S/C) :")
vivienda = input(" Introduzca si vive en campo o ciudad (U/R) :")


if (añosbanco >= 10 and hijos >= 2):
    print("APROBADO")
elif (estado_c == "c" or estado_c == "C" and  hijos > 3 and nacimiento >= 1975 and nacimiento <= 1965) :
    print("APROBADO")
elif (ingreso >= 2500000  and estado_c == "s" and vivienda == u):
    print("APROBADO")
elif (ingreso >= 3500000 and añosbanco > 5):
    print("APROBADO")
elif (vivienda == "r" or vivienda == "R" and estado_c == "C" or estado_c == "c" and hijos < 2):
    print("APROBADO")
else :
    print("NO APROBADO")




