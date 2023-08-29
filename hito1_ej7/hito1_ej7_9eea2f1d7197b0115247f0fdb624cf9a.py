#Zodiaco
día= int(input("Ingrese el día de su cumpleaños: "))
mes= int(input("Ingres el número del mes de su cumpleaños: "))

if mes==1:
    if día<31 and día>21:
        print("Acuario")
    else:
        print("Capricornio")

elif mes==2:
    if día<29 and día>19:
        print("Piscis")
    else:
        print("Acuario")

elif mes==3:
    if  día<31 and día>21:
        print("Aries")
    else:
        print("Piscis")

elif mes==4:
    if día<30 and día>21:
        print("Tauro")
    else:
        print("Aries")

elif mes==5:
    if día<31 and día>22:
        print("Geminis")
    else:
        print("Tauro")

elif mes==6:
    if día<30 and día>22:
        print("Cancer")
    else:
        print("Geminis")

elif mes==7:
    if día<31 and día>23:
        print("Leo")
    else:
        print("Cancer")

elif mes==8:
    if día<31 and día>23:
        print("Virgo")
    else:
        print("Leo")

elif mes==9:
    if día<30 and día>24:
        print("Libra")
    else:
        print("Virgo")

elif mes==10:
    if día<31 and día>24:
        print("Escorpio")
    else:
        print("Libra")

elif mes==11:
    if día<30 and día>23:
        print("Sagitario")
    else:
        print("Escorpio")

elif mes==12:
    if día<31 and día>22:
        print("Capricornio")
    else:
        print("Sagitario")