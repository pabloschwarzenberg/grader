#Zodiaco
def signo_zodiaco(dia,mes):
    if mes == 1:
        if dia<=20:
            signo= "Capricornio"
        else:
            signo="Acuario"
    elif mes==2:
        if dia<=19:
            signo="Acuario"
        else:
            signo="Piscis"
    elif mes==3:
        if dia<=20:
            signo="Piscis"
        else:
            signo="Aries"
    elif mes==4:
        if dia<=21:
            signo="Aries"
        else:
            signo="Tauro"
    elif mes==5:
        if dia<=21:
            signo="Tauro"
        else:
            signo="Geminis"
    elif mes==6:
        if dia<=21:
            signo="Geminis"
        else:
            signo="Cancer"
    elif mes==7:
        if dia <=22:
            signo="Cancer"
        else:
            signo="Leo"
    elif mes==8:
        if dia<=22:
            signo="Leo"
        else:
            signo="Virgo"
    elif mes==9:
        if dia <=22:
            signo="Virgo"
        else:
            signo="Libra"
    elif mes==10:
        if dia<=22:
            signo="Libra"
        else:
            signo="Escorpio"
    elif mes ==11:
        if dia <= 22:
            signo="Escorpio"
        else:
            signo="Sagitario"
    elif mes ==12:
        if dia <=21:
            signo="Sagitario"
        else:
            signo="Capricornio"

    return signo
print("Ingrese su fecha de nacimiento en numeros enteros")
dia = int(input("Dia: "))
mes = int(input("Mes: "))

signo = signo_zodiaco(dia,mes)
print("Tu signo zodiacal es ", signo)
