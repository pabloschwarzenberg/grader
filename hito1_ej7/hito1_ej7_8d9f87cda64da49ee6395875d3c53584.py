#Zodiaco
dia = int(input("Ingrese día de su cumpleaños:"))
mes = int(input("Ingrese mes de su cumpleaños, en número:"))
if ((mes==3) and (dia>=21) or (mes==4) and (dia<=20)):
    print("Signo zodiacal: ARIES")
else:
    if ((mes==4) and (dia>=20) or (mes==5) and (dia<=21)):
        print("Signo zodiacal: TAURO")
    else:
        if ((mes==5) and (dia>=21) or (mes==6) and (dia<=21)):
            print("Signo zodiacal:GEMIINIS")
        else:
            if ((mes==6) and (dia>21) or (mes==7) and (dia<=23)):
                print("Signo zodiacal: CANCER")
            else:
                if ((mes==7) and (dia>=23) or (mes==8) and (dia<=23)):
                    print("Signo zodiacal: LEO")
                else:
                    if ((mes==8) and (dia>=23) or (mes==9) and (dia<=23)):
                        print("Signo zodiacal: VIRGO")
                    else:
                        if ((mes==9) and (dia>=23) or (mes==10) and (dia<=23)):
                            print("Signo zodiacal: LIBRA")
                        else:
                            if ((mes==10) and (dia>=23) or (mes==11) and (dia<=22)):
                                print("Signo zodiacal: ESCORPIO")
                            else:
                                if ((mes==11) and (dia>=22) or (mes==12) and (dia<=22)):
                                    print("Signo zodiacal: SAGITARIO")
                                else:
                                    if ((mes==12) and (dia>=22) or (mes==1) and (dia<=20)):
                                        print("Signo zodiacal: CAPRICORNIO")
                                    else:
                                        if ((mes==1) and (dia>=20) or (mes==2) and (dia<=19)):
                                            print("Signo zodiacal: ACUARIO")
                                        else:
                                            if ((mes==2) and (dia>=19) or (mes==3) and (dia<=21)):
                                                print("Signo zodiacal: PISCIS")      