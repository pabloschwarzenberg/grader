#Signos zodiacales

signo = ["Capricornio" , "Acuario" , " Piscis" , "Aries" , "Tauro" , "Geminis" , "Cancer" ,"Leo" , "Virgo" , "Libra" , "Escorpio" , "Sagitario" ]
fecha = [20,19,20,20,21,21,22,22,22,22,22,21]

#Datos del usuario

dia= int(input("Dia de nacimiento:"))
mes= int(input("Mes de nacimiento:"))

mes = mes -1
if dia > fecha[mes]:
    mes = mes +1
if mes == 12:
    mes= 0

#resultado
print("Su signo zodiacal es", signo[mes])