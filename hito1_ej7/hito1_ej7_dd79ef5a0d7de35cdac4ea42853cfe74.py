dia=int(input("Ingrese dia de cumpleaños: "))
if not dia<1 and dia>31:
    print("error")
else:
    mes=int(input("Ingrese el mes de su cumpleaños 1 al 12 en donde 1 es enero: "))
    if not mes<1 and mes>12:
        print("error")
    else:
        if mes==3:
            if dia>=21 and dia<30:
                print("Aries")
            else:
                print("Piscis")
        if mes==4:
            if dia>=1 and dia<20:
                print("Aries")
            else:
                print("Tauro")
        if mes==5:
            if dia>=1 and dia<21:
                print("Tauro")
            else:
                print("Geminis")
        if mes==6:
            if dia>=1 and dia<21:
                print("Geminis")
            else:
                print("Cancer")
        if mes==7:
            if dia>=1 and dia<23:
                print("Cancer")
            else:
                print("Leo")
        if mes==8:
            if dia>=1 and dia<23:
                print("Leo")
            else:
                print("Virgo")
        if mes==9:
            if dia>=1 and dia<23:
                print("Virgo")
            else:
                print("Libra")
        if mes==10:
            if dia>=1 and dia<23:
                print("Libra")
            else:
                print("Escorpion")
        if mes==11:
            if dia>=1 and dia<22:
                print("Escorpion")
            else:
                print("Sagitario")
        if mes==12:
            if dia>=1 and dia<22:
                print("Sagitario")
            else:
                print("Capricornio")
        if mes==1:
            if dia>=1 and dia<20:
                print("Capricornio")
            else:
                print("Acuario")
        if mes==2:
            if dia>=1 and dia<19:
                print("Acuario")
            else:
                print("Piscis")
        