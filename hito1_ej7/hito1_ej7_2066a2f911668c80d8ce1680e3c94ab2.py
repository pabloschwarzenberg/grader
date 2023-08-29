#Zodiaco
dia = int(input("Ingrese dia: "))
mes = int(input("Ingrese mes: "))


if mes == 3 and dia >= 21 or mes == 4 and dia <= 20:
    print("Su signo del zodiaco es ARIES")
elif mes == 4  and dia >= 20 or mes == 5 and dia <= 21:
    print("Su signo del zodiaco es TAURO")
elif mes == 5 and dia >= 21 or mes == 6 and dia <= 21:
    print("Su signo del zodiaco es GEMENIS")
elif mes == 6 and dia >= 21 or mes == 7 and dia <= 23:
    print("Su signo del zodiaco es CANCER")
elif mes == 7 and dia >= 23 or mes == 8 and dia <= 23:
    print("Su signo del zodiaco es LEO")
elif mes == 8 and dia >= 23 or mes == 9 and dia <= 23:
    print("Su signo del zodiaco es VIRGO")
elif mes == 9 and dia >=23 or mes == 10 and dia <= 23:
    print("Su signo del zodiaco es  LIBRA")
elif mes == 10 and dia >= 23 or mes == 11 and dia <= 23:
    print("Su signo del zodiaco es ESCORPIO")
elif mes == 11 and dia >= 23 or mes == 12 and dia <= 22:
    print("Su signo del zodiaco es SAGITARIO")
elif mes == 12 and dia >= 22 or mes == 1 and dia <= 20:
    print("Su signo del zodiaco es CAPRICORNIO")
elif mes == 1 and dia >= 20 or mes == 2 and dia <= 19:
    print("Su signo del zodiaco es ACUARIO")
elif mes == 2 and dia >= 19 or mes == 3 and dia <=21:
    print("Su signo del zodiaco es PISCIS")
else:
    print("El dia y mes estan incorrectos")      