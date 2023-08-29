#Zodiaco
def signo_zodiacal(dia,mes):
    if mes == 1 and dia<=20:
        signo= "Capricornio"
    elif mes==1 and dia>20:
        signo="Acuario"
    elif mes==2 and dia<=19:
        signo="Acuario"
    elif mes ==2 and dia >19:
        signo="Picis"
    elif mes==3 and dia<=20:
        signo="Picis"
    elif mes==3 and dia>20:
        signo="Aries"
    elif mes==4 and dia<=21:
        signo="Aries"
    elif mes==4 and dia>21:
        signo="Tauro"
    elif mes==5 and dia<=21:
        signo="Tauro"
    elif mes==5 and dia>21:
        signo="Géminis"
    elif mes==6 and dia<=21:
        signo="Géminis"
    elif mes==6 and dia>21:
        signo="Cáncer"
    elif mes==7 and dia <=22:
        signo="Cáncer"
    elif mes== 7 and dia >22:
        signo="Leo"
    elif mes==8 and dia<=22:
        signo="Leo"
    elif mes==8 and dia>22:
        signo="Virgo"
    elif mes==9 and dia <=22:
        signo="Virgo"
    elif mes==9 and dia>22:
        signo="Libra"
    elif mes==10 and dia<=22:
        signo="Libra"
    elif mes==10 and dia>22:
        signo="Escorpio"
    elif mes ==11 and dia <= 22:
        signo="Escorpio"
    elif mes==11 and dia>22:
        signo="Sagitario"
    elif mes ==12 and dia <=21:
        signo="Sagitario"
    else:
        signo="Capricornio"

    return signo
print("Ingrese su fecha de nacimiento en numeros enteros")
dia = int(input("Dia: "))
mes = int(input("Mes: "))


signo = signo_zodiacal(dia,mes)
print(signo)
