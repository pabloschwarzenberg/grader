#Zodiaco
dia= int(input("Ingrese el dia que nació (1 al 31): "))
mes= int(input("Ingrese el mes que nacio (1 al 12): "))
if mes == 3 and dia >= 21 and dia <= 31 or mes == 4 and dia >=1 and dia<=19:
    print("Tu signo zodiacal es Aries.")
else:
    if mes == 4 and dia >= 20 and dia <= 30 or mes == 5 and dia >=1 and dia<=20:
        print("Tu signo zodiacal es Tauro.")
    else:
        if mes == 5 and dia >= 21 and dia <= 31 or mes == 6 and dia >=1 and dia<=20:
            print("Tu signo zodiacal es Géminis.")
        else:
            if mes == 6 and dia >= 21 and dia <= 30 or mes == 7 and dia >=1 and dia<=22:
                print("Tu signo zodiacal es Cáncer.")
            else:
                if mes == 7 and dia >= 23 and dia <= 31 or mes == 8 and dia >=1 and dia<=22:
                    print("Tu signo zodiacal es Leo.")
                else:
                    if mes == 8 and dia >= 23 and dia <= 31 or mes == 9 and dia >=1 and dia<=22:
                        print ("Tu signo zodiacal es Virgo.")
                    else:
                        if mes == 9 and dia >= 23 and dia <= 30 or mes == 10 and dia >=1 and dia<=22:
                            print("Tu signo zodiacal es Libra.")
                        else:
                            if mes == 10 and dia >= 23 and dia <= 31 or mes == 11 and dia >=1 and dia<=21:
                                print("Tu signo zodiacal es Escorpio.")
                            else:
                                if mes == 11 and dia >= 22 and dia <= 30 or mes == 12 and dia >=1 and dia<=21:
                                    print("Tu signo zodiacal es Sagitario.")
                                else:
                                    if mes == 12 and dia >= 22 and dia <= 31 or mes == 1 and dia >=1 and dia<=19:
                                        print("Tu signo zodiacal es Capricornio.")
                                    else:
                                        if mes == 1 and dia >= 20 and dia <= 31 or mes == 2 and dia >=1 and dia<=18:
                                            print("Tu signo zodiacal es Acuario.")
                                        else:
                                            if mes == 2 and dia >= 19 and dia <= 28 or mes == 3 and dia >=1 and dia<=20:
                                                print("Tu signo zodiacal es Piscis")
                                            else:
                                                print("Los datos no son correctos")      