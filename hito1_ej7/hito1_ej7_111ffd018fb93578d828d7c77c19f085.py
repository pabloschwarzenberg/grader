#Zodiaco
dia = int(input("ingrese el dia de su nacimiento : "))
mes = int(input("ingrese el numero del mes en el que nacio : "))
if mes == 3 and dia >= 21 and dia <=31 or mes == 4 and dia >= 1 and dia <= 20:
    print("aries")
else:
    if mes == 4 and dia >= 20 and dia <= 30 or mes == 5 and dia >= 1 and dia <= 20:
        print("tauro")
    else:
        if mes == 5 and dia >= 21 and dia <= 31 or mes == 6 and dia >= 1 and dia <= 20:
            print("geminis")
        else:
            if mes == 6 and dia >= 21 and dia <= 30 or mes == 7 and dia >= 1 and dia <= 22:
                print("cancer")
            else:
                if mes == 7 and dia >= 23 and dia <= 31 or mes == 8 and dia >= 1 and dia <= 22:
                    print("leo")
                else:
                    if mes == 8 and dia >= 23 and dia <= 31 or mes == 9 and dia >= 1 and dia <= 22:
                        print("virgo")
                    else:
                        if mes == 9 and dia >= 23 and dia <= 30 or mes == 10 and dia >= 1 and dia <= 22:
                            print("libra")
                        else:
                            if mes == 10 and dia >= 23 and dia <= 31 or mes == 11 and dia >= 1 and dia <= 21:
                                print("escorpio")
                            else:
                                if mes == 11 and dia >= 22 and dia <= 30 or mes == 12 and dia >= 1 and dia <= 21:
                                    print("sagitario")
                                else:
                                    if mes == 12 and dia >= 22 and dia <= 30 or mes == 1 and dia >= 1 and dia <= 19:
                                        print("capricornio")

