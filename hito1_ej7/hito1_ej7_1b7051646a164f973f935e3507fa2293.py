dia = int(input("Ingrese Dia de Nacimiento"))
mes = int(input("Ingrese mes de Nacimiento"))

if   dia >= 21 and mes == 3  or dia <= 20 and mes == 4:
    mensaje ="Aries"
elif dia >= 21 and mes == 4  or dia <= 20 and mes == 5:
    mensaje ="Tauro"
elif dia >= 21 and mes == 5  or dia <= 21 and mes == 6:
    mensaje ="Geminis"
elif dia >= 22 and mes == 6  or dia <= 22 and mes == 7:
    mensaje ="Cancer"
elif dia >= 23 and mes == 7  or dia <= 23 and mes == 8:
    mensaje ="Leo"
elif dia >= 24 and mes == 8  or dia <= 22 and mes == 9:
    mensaje ="Virgo"
elif dia >= 23 and mes == 9  or dia <= 22 and mes == 10:
    mensaje ="Libra"
elif dia >= 23 and mes == 10 or dia <= 22 and mes == 11:
    mensaje ="Escorpio"
elif dia >= 23 and mes == 11 or dia <= 21 and mes == 12:
    mensaje ="Sagitario"
elif dia >= 22 and mes == 12 or dia <= 20 and mes == 1:
    mensaje ="Capricornio"
elif dia >= 21 and mes == 1  or dia <= 19 and mes == 2:
    mensaje ="Acuario"
elif dia >= 20 and mes == 2  or dia <= 20 and mes == 3:
    mensaje ="Piscis"
else:
     mensaje = "Fecha Incorrecta"



print(mensaje)