#Zodiaco
def signo_zodiacal(dia,mes):
    if mes == 1:
        if dia<=20:
            signo="capricornio"
        else:
            signo="acuario"
    elif mes==2:
        if dia<=19:
            signo="acuario"
        else:
            signo="picis"
    elif mes==3:
        if dia<=20:
            signo="picis"
        else:
            signo="aries"
    elif mes==4:
        if dia<=21:
            signo="aries"
        else:
            signo="tauro"
    elif mes==5:
        if dia<=21:
            signo="tauro"
        else:
            signo="geminis"
    elif mes==6:
        if dia<=21:
            signo="geminis"
        else:
            signo="cancer"
    elif mes==7:
        if dia <=22:
            signo="cancer"
        else:
            signo="leo"
    elif mes==8:
        if dia<=22:
            signo="leo"
        else:
            signo="virgo"
    elif mes==9:
        if dia <=22:
            signo="virgo"
        else:
            signo="libra"
    elif mes==10:
        if dia<=22:
            signo="libra"
        else:
            signo="escorpio"
    elif mes ==11:
        if dia <= 22:
            signo="escorpio"
        else:
            signo="sagitario"
    elif mes ==12:
        if dia <=21:
            signo="sagitario"
        else:
            signo="capricornio"

    return signo
print("Ingrese su fecha de nacimiento en numeros enteros")
dia = int(input("Dia: "))
mes = int(input("Mes: "))
anio = int(input("Año: "))

signo = signo_zodiacal(dia,mes)
print(signo)