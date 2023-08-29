#Zodiaco
dia = int(input("Ingrese el dia en que nacio"))
mes = int(input("Ingrese el mes en que nacio"))
if 22 <= dia <= 31 and mes == 3 or 1 <= dia <= 20 and mes == 4 :
    print("Su signo del zodiaco es Aries")
else :
    if 21 <= dia <= 30 and mes == 4 or 1 <= dia <= 21 and mes == 5 :
        print("Su signo del zodiaco es Tauro")
    else :
        if 22 <= dia <= 31 and mes == 5 or 1 <= dia <= 21 and mes == 6 :
            print("Su signo del zodiaco es Geminis")
        else :
            if 22 <= dia <= 30 and mes == 6 or 1 <= dia <= 23 and mes == 7 :
                print("Su signo del zodiaco es Cancer")
            else:
                if 24 <= dia <= 31 and mes == 7 or 1 <= dia <= 23 and mes == 8 :
                    print("Su signo del zodiaco es Leo")
                else:
                    if 24 <= dia <= 31 and mes == 8 or 1 <= dia <= 23 and mes == 9 :
                        print("Su signo del zodiaco es Virgo")
                    else:
                        if 24 <= dia <= 30 and mes == 9 or 1 <= dia <= 23 and mes == 10 :
                            print("Su signo del zodiaco es Libra")
                        else:
                            if 24 <= dia <= 31 and mes == 10 or 1 <= dia <= 22 and mes == 11 :
                                print("Su signo del zodiaco es Escorpio")
                            else:
                                if 23 <= dia <= 30 and mes == 11 or 1 <= dia <= 22 and mes == 12 :
                                    print("Su signo del zodiaco es Sagitario")
                                else:
                                    if 22 <= dia <= 31 and mes == 12 or 1 <= dia <= 20 and mes == 1 :
                                        print("Su signo del zodiaco es Capricornio")
                                    else:
                                        if 21 <= dia <= 31 and mes == 1 or 1 <= dia <= 19 and mes == 2 :
                                            print("Su signo del zodiaco es Acuario")
                                        else:
                                            if 20 <= dia <= 29 and mes == 2 or 1 <= dia <= 21 and mes == 3 :
                                                print("Su signo del zodiaco es Piscis")
                                            else:
                                                print("Ingrese un valor valido")