#Zodiaco
def signo_del_zodiaco(dia, mes):
    if (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        print("Su signo del zodíaco es Acuario")
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        print("Su signo del zodíaco es Piscis")
    elif (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        print("Su signo del zodíaco es Aries")
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        print("Su signo del zodíaco es Tauro")
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        print("Su signo del zodíaco es Geminis")
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        print("Su signo del zodíaco es Cancer")
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        print("Su signo del zodíaco es Leo")
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        print("Su signo del zodíaco es Virgo")
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        print("Su signo del zodíaco es Libra")
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        print("Su signo del zodíaco es Escorpio")
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        print("Su signo del zodíaco es Sagitario")
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        print("Su signo del zodiaco es Capricornio")
    else:
        print("fecha inexistente")
#colocar las condicionantes segun la fecha de cumpleaños para saber que signo es 
#y si coloca una fecha fuera de los limites que sea incorrecta 

dia = int(input("Ingrese el día de cumpleaños: "))
mes = int(input("Ingrese el mes de cumpleaños: "))
#preguntar el dia y el mes de cumpleaños de la persona

signo = signo_del_zodiaco(dia, mes)