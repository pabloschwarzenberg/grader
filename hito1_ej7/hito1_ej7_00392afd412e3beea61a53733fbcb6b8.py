#Zodiaco
dia = int(input("Ingrese el dia de su nacimiento como numero entero: "))
mes =  int(input("Ingrese el mes de su nacimiento como numero entero: "))

if ((mes==3) and (dia>=22)) or((mes==4) and (dia<=20)):
    print ("ARIES")

else:
    if ((mes==4) and (dia>=21)) or((mes==5) and (dia<=21)):
        print ("TAURO")

    else:
        if ((mes==5) and (dia>=22)) or((mes==6) and (dia<=21)):
            print ("GEMINIS")

        else:
            if ((mes==6) and (dia>=22)) or((mes==7) and (dia<=23)):
                print ("CANCER")

            else:
                if ((mes==7) and (dia>=24)) or((mes==8) and (dia<=23)):
                    print ("LEO")

                else:
                    if ((mes==8) and (dia>=24)) or((mes==9) and (dia<=23)):
                        print ("VIRGO")

                    else:
                        if ((mes==9) and (dia>=24)) or((mes==10) and (dia<=23)):
                            print ("LIBRA")

                        else:
                            if ((mes==10) and (dia>=24)) or((mes==11) and (dia<=22)):
                                print ("ESCORPIO")

                            else:
                                if ((mes==11) and (dia>=24)) or((mes==12) and (dia<=22)):
                                    print ("SAGITARIO")

                                else:
                                    if ((mes==12) and (dia>=23)) or((mes==1) and (dia<=20)):
                                        print ("CAPRICORNIO")

                                    else:
                                        if ((mes==1) and (dia>=21)) or((mes==2) and (dia<=19)):
                                            print ("ACUARIO")

                                        else:
                                            if ((mes==2) and (dia>=20)) or((mes==3) and (dia<=21)):
                                                print ("PISCIS")
 