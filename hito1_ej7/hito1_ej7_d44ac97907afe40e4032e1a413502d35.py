dia = int(input("Ingrese su dia de cumpleaños: "))
mes = int(input("Ingrese su mes de nacimiento: "))
signo = ""
if mes == 3 and dia >= 21:
    signo = "aries"
if mes == 4 and dia <= 20:
    signo = "aries"
if mes == 4 and dia >= 21:
    signo = "tauro"
if mes == 5 and dia <= 20:
    signo = "tauro"
if mes == 5 and dia >= 21:
    signo = "geminis"
if mes == 6 and dia <=20:
    signo = "geminis"
if mes == 6 and dia >= 22:
    signo = "cancer"
if mes == 7 and dia <= 22:
    signo = "cancer"
if mes == 7 and dia >= 23:
    signo = "leo"
if mes == 8 and dia <= 22:
    signo = "leo"
if mes == 8 and dia >=23:
    signo = "virgo"
if mes == 9 and dia <= 22:
    signo = "virgo"
if mes == 9 and dia >= 23:
    signo = "libra"
if mes == 10 and dia <=22:
    signo = "libra"
if mes == 10 and dia >= 23:
    signo = "escorpio"
if mes == 11 and dia <= 22:
    signo = "escorpio"
if mes == 11 and dia >= 23:
    signo = "sagitario"
if mes == 12 and dia <= 21:
    signo = "sagitario"
if mes == 12 and dia >= 22:
    signo = "carpicornio"
if mes == 1 and dia <= 20:
    signo = "capricornio"
if mes == 1 and dia >= 21:
    signo = "acuario"
if mes == 2 and dia <=18:
    signo = "acuario"
if mes == 2 and dia >= 19:
    signo = "piscis"
if mes == 3 and dia <= 20:
    signo = "piscis"

print(signo)