#Zodiaco
dia = int(input("Ingrese día de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento en número: "))

if ((mes == 3) and (dia >= 21)) or ((mes == 4) and (dia <= 20)):
    signo = "aries"
    print(signo)
elif ((mes == 4) and (dia >= 20)) or ((mes == 5) and (dia <= 21)):
    signo = "tauro"
    print(signo)
elif ((mes == 5) and (dia >= 21)) or ((mes == 6) and (dia <= 21)):
    signo = "geminis"
    print(signo)
elif ((mes == 6) and (dia >= 21)) or ((mes == 7) and (dia <= 23)):
    signo = "cancer"
    print(signo)
elif ((mes == 7) and (dia >= 23)) or ((mes == 8) and (dia <= 23)):
    signo = "leo"
    print(signo)
elif ((mes == 8) and (dia >= 23)) or ((mes == 9) and (dia <= 23)):
    signo = "virgo"
    print(signo)
elif ((mes == 9) and (dia >= 23)) or ((mes == 10) and (dia <= 23)):
    signo = "libra"
    print(signo)
elif ((mes == 10) and (dia >= 23)) or ((mes == 11) and (dia <= 22)):
    signo = "escorpio"
    print(signo)
elif ((mes == 11) and (dia >= 23)) or ((mes == 12) and (dia <= 22)):
    signo = "sagitario"
    print(signo)
elif ((mes == 12) and (dia >= 22)) or ((mes == 1) and (dia <= 20)):
    signo = "capricornio"
    print(signo)
elif ((mes == 1) and (dia >= 20)) or ((mes == 2) and (dia <= 19)):
    signo = "acuario"
    print(signo)
elif ((mes == 2) and (dia >= 19)) or ((mes == 3) and (dia <= 21)):
    signo = "piscis"
    print(signo)
else:
    print("La fecha que usted ha ingresado no es correcta.")