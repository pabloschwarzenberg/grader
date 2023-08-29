#Zodiaco
dia=int(input("Ingrese el día de nacimiento: "))
mes=int(input("Ingrese el mes de nacimiento: "))

#Calculo
if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
    signo = "Aries"
elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
    signo = "Tauro"
elif (mes == 5 and dia >= 20) or (mes == 6 and dia <= 21):
    signo = "Géminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 23):
    signo = "Cáncer"
elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
    signo = "Leo"
elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 23):
    signo = "Virgo"
elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 23):
    signo = "Libra"
elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
    signo = "Escorpio"
elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 22):
    signo = "Sagitario"
elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
    signo = "Capricornio"
elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 19):
    signo = "Acuario"
else:
    signo = "Piscis"
print("Su signo es: ", signo)