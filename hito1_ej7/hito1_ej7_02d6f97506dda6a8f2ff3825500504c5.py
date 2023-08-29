#Zodiaco
dia= int(input("Ingrese día de nacimiento:"))
mes= int(input("Ingrese mes de nacimiento:"))

if (dia >=21 and mes == 3) or (mes == 4 and dia <=19):
    signo= "Aries"

elif (dia >= 20 and mes == 4) or (mes == 5 and dia <=20):
    signo = "Tauro"

elif (dia >= 21 and mes == 5) or (mes == 6 and dia <=20):
    signo = "Geminis"
    
elif (dia >= 21 and mes == 6) or (mes == 7 and dia <=22):
    signo = "Cancer"

elif (dia >= 23 and mes == 7) or (mes == 8 and dia <=22):
    signo = "Leo"

elif (dia >= 23 and mes == 8) or (mes == 9 and dia <=22):
    signo = "Virgo"

elif (dia >= 23 and mes == 9) or (mes == 10 and dia <=22):
    signo = "Libra"
    
elif (dia >= 23 and mes == 10) or (mes == 11 and dia <=21):
    signo = "Escorpio"

elif (dia >= 22 and mes == 11) or (mes == 12 and dia <=21):
    signo = "Sagitario"


elif (dia >= 22 and mes == 12) or (mes == 1 and dia <=19):
    signo = "Capricornio"

elif (dia >= 20 and mes == 1) or (mes == 2 and dia <=19):
    signo = "Acuarios"

elif (dia >= 19 and mes == 2) or (mes == 3 and dia <=20):
    signo = "Piscis"

print (signo)