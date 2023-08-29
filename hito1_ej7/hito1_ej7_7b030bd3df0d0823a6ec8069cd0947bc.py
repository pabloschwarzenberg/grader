#Zodiaco
dia = int(input("Ingrese dia de cumpleaños: "))
mes = int(input("Ingrese mes de cumpleaños: "))

enero = 1
febrero = 2
marzo = 3
abril = 4
mayo = 5
junio = 6
julio = 7
agosto = 8
septiembre = 9
octubre = 10
noviembre = 11
diciembre = 12

if((dia >= 21 and dia > 0 and marzo == mes)):
    print("Aries")
if((dia <= 20 and dia > 0 and mes == abril)):
    print("Aries")
else:
    if((dia >= 20 and dia > 0 and abril == mes)):
        print("Tauro")
    if((dia <= 21 and dia > 0 and mes == mayo)):
        print("Tauro")  
    else:
        if((dia >= 21 and dia > 0 and mayo == mes)):
            print("Geminis")
        if((dia <= 21 and dia > 0 and mes == junio)):
            print("Geminis")
        else:
            if((dia >= 21 and dia > 0) and (junio == mes)):
                print("Cancer")
            if((dia <= 23 and dia > 0) and (mes == julio)):
                print("Cancer")
            else:
                if((dia >= 23 and dia > 0) and (julio == mes)):
                    print("Leo")
                if((dia <= 23 and dia > 0) and (mes == agosto)):
                    print("Leo")
                else:
                    if((dia >= 23 and dia > 0) and (agosto == mes)):
                        print("Virgo")
                    if((dia <= 23 and dia > 0) and (mes == septiembre)):
                        print("Virgo")
                    else:
                        if((dia >= 23 and dia > 0) and (septiembre == mes)):
                            print("Libra")
                        if((dia <= 23 and dia > 0) and (mes == octubre)):
                            print("Libra")
                        else:
                            if((dia >= 23 and dia > 0) and (octubre == mes)):
                                print("Escorpion")
                            if((dia <= 22 and dia > 0) and (mes == noviembre)):
                                print("Escorpion")
                            else:
                                if((dia >= 23 and dia > 0) and (noviembre == mes)):
                                    print("Sagitario")
                                if((dia <= 22 and dia > 0) and (mes == diciembre)):
                                    print("Sagitario")
                                else:
                                    if((dia >= 22 and dia > 0) and (diciembre == mes)):
                                        print("Capricornio")
                                    if((dia <= 20 and dia > 0) and (mes == enero)):
                                        print("Capricornio")
                                    else:
                                        if((dia >= 20 and dia > 0) and (enero == mes)):
                                            print("Aquario")
                                        if((dia <= 19 and dia > 0) and (mes == febrero)):
                                            print("Aquario")
                                        else:
                                            if((dia >= 19 and dia > 0) and (febrero == mes)):
                                                print("Pisces")
                                            if((dia <= 21 and dia > 0) and (mes == marzo)):
                                                print("Pisces")