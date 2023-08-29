#Zodiaco
#ENTRADA
dia = int(input("ingrese el dia de su nacimiento (numero): "))
mes = int(input("ingrese el mes de su nacimiento (numero): "))


#PROCESO
signo = ""
if (mes == 3 and dia >= 21) or (mes == 4 and dia < 20):
    signo = "Aries"
elif (mes == 4 and dia >= 21) or (mes == 5 and dia < 20):
    signo = "Tauro"
elif (mes == 5 and dia >= 21) or (mes == 6 and dia < 20):
    signo = "Geminis"
elif (mes == 6 and dia >= 21) or (mes == 7 and dia < 20):
    signo = "Cancer"
elif (mes == 7 and dia >= 21) or (mes == 8 and dia < 20):
    signo = "Leo"
elif (mes == 8 and dia >= 21) or (mes == 9 and dia < 20):
    signo = "Virgo"
elif (mes == 9 and dia >= 21) or (mes == 10 and dia < 20):
    signo = "Libra"
elif (mes == 10 and dia >= 21) or (mes == 11 and dia < 20):
    signo = "Escorpio"
elif (mes == 11 and dia >= 21) or (mes == 12 and dia < 20):
    signo = "Sagitario"
elif (mes == 12 and dia >= 21) or (mes == 1 and dia < 20):
    signo = "Capricornio"
elif (mes == 1 and dia >= 21) or (mes == 2 and dia < 20):
    signo = "Acuario"
elif (mes == 2 and dia >= 21) or (mes == 3 and dia < 20):
    signo = "piscis"

#SALIDA
print(signo)
