#Zodiaco
dia = int(input("ingrese el dia de su cumpleaños: "))
mes = int(input("ingrese su mes de cumpleaños con numeros (1 al 12): "))
if (dia > 21 and dia <=31 and mes == 3) or ( dia >= 1 and dia <=20  and mes ==4):
    print("Aries")
else:
    if (dia >= 21 and dia <= 31 and mes == 4) or (dia >= 1 and dia <= 21 and mes == 5):
        print("Tauros")
    else:
        if (dia > 21 and dia <= 31 and mes == 5) or (dia >= 1 and dia <= 21 and mes == 6):
            print("Gemini")
        else:
            if (dia > 21 and dia <= 31 and mes == 6) or (dia >= 1 and dia <= 23 and mes == 7):
                print("Cancer")
            else:
                if (dia > 23 and dia <= 31 and mes == 7) or (dia >= 1 and dia <= 23 and mes == 8):
                    print("Leo")
                else:
                    if (dia > 23 and dia <= 31 and mes == 8) or (dia >= 1 and dia <= 23 and mes == 9):
                        print("Virgo")
                    else:
                        if (dia > 23 and dia <= 31 and mes == 9) or (dia >= 1 and dia <= 23 and mes == 10):
                            print("Libra")
                        else:
                            if (dia > 23 and dia <= 31 and mes == 10) or (dia >= 1 and dia <= 22 and mes == 11):
                                print("escorpio")
                            else:
                                if (dia > 22 and dia <= 31 and mes == 11) or (dia >= 1 and dia <= 22 and mes == 12):
                                    print("Sagitario")
                                else:
                                    if (dia > 2 and dia <= 31 and mes == 12) or (dia >= 1 and dia <= 20 and mes == 1):
                                        print("Capricornio")
                                    else:
                                        if (dia > 20 and dia <= 31 and mes == 1) or (dia >= 1 and dia <= 19 and mes == 2):
                                            print("Acuario")
                                        else:
                                            if (dia > 19 and dia <= 31 and mes == 2) or (dia >= 1 and dia <= 21 and mes == 3):
                                                print("Piscis")