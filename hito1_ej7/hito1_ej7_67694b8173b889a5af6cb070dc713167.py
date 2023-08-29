#Zodiaco
dia = int(input("Ingresa tu dia de nacimiento: "))
mes = int(input("Ingres tu mes de nacimiento, numericamente(ex: Enero = 1): "))
#Enero, marzo, mayo, julio, agosto, octubre y diciembre

if mes == 2 and dia < 29:
    print("numero no valido")
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 and dia < 32:
    print("Numero no valido")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11 and  dia < 31:
    print("Numero no valido")

if dia >= 21 and mes == 3 or dia < 20 and mes == 4:
    print("Tu signo es Aries")
elif dia >= 20 and mes == 4 or dia < 21 and mes == 5:
     print("Tu signo es Tauro")
elif dia >= 21 and mes == 5 or dia < 21 and mes == 6:
    print("Tu signo es Geminis")
elif dia >= 21 and mes == 6 or dia < 23 and mes == 7:
    print("Tu signo es Cancer")
elif dia >= 23 and mes == 7 or dia < 23 and mes == 8:
    print("Tu signo es Leo")
elif dia >= 23 and mes == 8 or dia < 23 and mes == 9:
    print("Tu signo es Virgo")
elif dia >= 23 and mes == 9 or dia < 23 and mes == 10:
    print("Tu signo es Libra")
elif dia >= 23 and mes == 10 or dia < 22 and mes == 11:
    print("Tu signo es Escorpio")
elif dia >= 23 and mes == 11 or dia < 22 and mes == 12:
    print("Tu signo es Sagitario")
elif dia >= 22 and mes == 12 or dia < 20 and mes == 1:
    print("Tu signo es Capricornio")
elif dia >= 20 and mes == 1 or dia < 19 and mes == 2:
    print("Tu signo es Acuario")
elif dia >= 19 and mes == 2 or dia < 21 and mes == 3:
    print("Tu signo es Piscis")
else:
    print("digitos ingresados no validos, intente nuevamente")
   
      