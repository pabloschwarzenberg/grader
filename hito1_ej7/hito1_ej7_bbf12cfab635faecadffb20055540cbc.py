dia = int(input("Ingrese el dia de su nacimiento con numeros: "))
mes = int(input("Ingrese el mes de su nacimiento con un numero: "))
if mes==3 and dia > 20 or mes==4 and dia < 21:
    print("Aries")
else:
    if mes==4 and dia > 19 or mes==5 and dia < 22:
        print("Tauro")
    else:
        if mes==5 and dia > 20 or mes==6 and dia<22:
            print("Geminis")
        else:
            if mes==6 and dia > 20 or mes==7 and dia <24:
                print("cancer")
            else:
                if mes==7 and dia > 22 or mes==8 and dia < 24:
                   print("leo")
                else:
                    if mes==8 and dia > 22 or mes==9 and dia < 24:
                        print("virgo")
                    else:
                        if mes==9 and dia > 22 or mes==10 and dia < 24:
                            print("libra")
                        else:
                            if mes==10 and dia> 22 or mes==11 and dia<23:
                                print("escorpion")
                            else:
                                if mes==11 and dia > 21 or mes==12 and dia < 23:
                                        print("sagitario")
                                else:
                                    if mes==12 and dia > 21 or mes==1 and dia < 21:
                                        print("capricornio")
                                    else:
                                        if mes==1 and dia > 19 or mes ==2 and dia < 22:
                                            print("acuario")
                                        else:
                                            if mes==2 and dia > 18 or mes==3 and dia <22:
                                                print("piscis")