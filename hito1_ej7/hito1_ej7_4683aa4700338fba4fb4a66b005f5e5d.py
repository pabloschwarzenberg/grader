#Zodiaco
def signo_zodiacal(mes, dia):

    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 20):
        return 'ARIES'

    elif (mes == 4 and dia >= 21) or (mes == 5 and dia <= 20):
        return 'TAURO'
    
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 21):
        return 'GEMINIS'

    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 23):
        return 'CANCER'
    
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 23):
        return 'LEO'
    
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 23):
        return 'VIRGO'
    
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 23):
        return 'LIBRA'
    
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 22):
        return 'ESCORPIO'
    
    elif (mes == 11 and dia >= 23) or (mes == 12 and dia <= 22):
        return 'SAGITARIO'

    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 20):
        return 'CAPRICORNIO'
    
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 19):
        return 'ACUARIO'
    
    else:
        return 'PICIS'

dia = int(input())
mes = int(input())
print(signo_zodiacal(mes, dia))