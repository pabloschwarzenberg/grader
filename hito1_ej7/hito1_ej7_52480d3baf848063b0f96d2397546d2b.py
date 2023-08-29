#Zodiaco
def algo_signo(dia, mes):
    signo =""
    if mes == 1:
        if dia <= 20:
            signo = "Capricornio"
        else:
            signo = "Acuario"
    elif mes == 2:
        if dia <= 19:
            signo = "Acuario"
        else:
            signo = "Pisis"
    elif mes == 3:
        if dia <= 21:
            signo = "Pisis"
        else:
            signo = "Aries"
    elif mes == 4:
        if dia <= 20:
            signo = "Aries"
        else:
            signo = "Tauro"
    elif mes == 5:
        if dia <= 21:
            signo = "Tauro"
        else:
            signo = "Geminis"
    elif mes == 6:
        if dia <= 21:
            signo = "Geminis"
        else:
            signo = "Cancer"
    elif mes == 7:
        if dia <= 23:
            signo = "Cancer"
        else:
            signo = "Leo"
    elif mes == 8:
        if dia <= 23:
            signo = "Leo"
        else:
            signo = "Virgo"
    elif mes == 9:
        if dia <= 23:
            signo = "Virgo"
        else:
            signo = "Libra"
    elif mes == 10:
        if dia <= 23:
            signo = "Libra"
        else:
            signo = "Escorpio"
    elif mes == 11:
        if dia <= 22:
            signo = "Escorpio"
        else:
            signo = "Sagitario"
    elif mes == 12:
        if dia <= 22:
            signo = "Sagitario"
        else:
            signo = "Capricornio"
    return signo

dia = int(input("Ingresa tu dia de nacimiento de forma numerica:\n"))
while (dia > 31) or (dia < 0):
    dia = int(input("Reintroduce tu dia de nacimiento:\n"))

mes = int(input("Ingresa tu mes de nacimiento:\n"))
while (mes > 12) or (mes < 0):
    mes = int(input("Reintroduce tu mes de nacimiento de forma numerica:\n"))

signito = algo_signo(dia, mes)

print("Tu signo zodiacal es",signito)