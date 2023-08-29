#SIGNO ZODIACAL
fecha=int(input("ingrese el dia de su cumpleaños del 1-31:"))
mes=int(input("ingrese el mes de su cumpleaños del 1-12:"))

if mes==3 and fecha>=21 and fecha<= 31 or mes ==4 and fecha>=1 and fecha<=19:
    print("el signo zodiacal correspondespondiente es ARIES")
else:
    if mes==4 and fecha>=20 and fecha<=30 or mes==5 and fecha>=1 and fecha<=20:
        print("el signo zodiacal correspondiente es TAURO")
    else:
        if mes==5 and fecha>=21 and fecha<=31 or mes==6 and fecha>=1 and fecha<=20:
           print("el signo sodiacal correspondiente es GEMINIS")
        else:
            if mes==6 and fecha>=21 and fecha<=30 or mes==7 and fecha>=1 and fecha<=22:
                print("el signo correspondiente es CANCER")
            else:
                if mes==7 and fecha>=23 and fecha<=31 or mes==8 and fecha>=1 and fecha<=22:
                    print("el signo correspondiente es LEO")
                else:
                    if mes==8 and fecha>=23 and fecha<=31 or mes==9 and fecha>=1 and fecha<=22:
                        print("el signo correspondiente es VIRGO")
                    else:
                        if mes==9 and fecha>=23 and fecha<=30 or mes==10 and fecha>=1 and fecha<=22:
                            print("el signo correspondiente es LIBRA")
                        else:
                            if mes==10 and fecha>=23 and fecha<=31 or mes==11 and fecha>=1 and fecha<=21:
                                print("el signo correspondiente es ESCORPIO")
                            else:
                                if mes==11 and fecha>=22 and fecha<=30 or mes==12 and fecha>=1 and fecha<=21:
                                    print("el signo correspondiente es SAGITARIO")
                                else:
                                    if mes==12 and fecha>=22 and fecha<=31 or  mes==1 and fecha>=1 and fecha<=19:
                                        print("el signo correspodiente es CAPRICORNIO")
                                    else:
                                        if mes==1 and fecha>=20 and fecha<=31 or mes==2 and fecha>=1 and fecha<=19:
                                           print("el signo correspondiente es ACUARIO")
                                        else:
                                            if mes==2 and fecha>=19 and fecha<=29 or mes==3 and fecha>=1 and fecha<=21:
                                               print("ele signo correspondiente es PISCIS")
