dia=int(input("Inserte dìa de nacimiento"))
mes=int(input("Inserte mes de nacimiento"))
if mes==1:
    if 1<=dia<=20:
        print("capricornio")
    elif 21<=dia<=31:
        print("acuario")
    else:
        print("dia invalido")
elif mes==2:
    if 1<=dia<=19:
        print("acuario")
    elif 20<=dia<=29:
        print("piscis")
    else:
        print("dia invalido")
elif mes==3:
    if 1<=dia<=20:
        print("piscis")
    elif 21<=dia<=31:
        print("aries")
    else:
        print("dia invalido")
elif mes==4:
    if 1<=dia<=20:
        print("aries")
    elif 21<=dia<30:
        print("tauro")
    else:
        print("dia invalido")
elif mes==5:
    if 1<dia<=21:
        print("tauro")
    elif 22<=dia<=31:
        print("gemimis")
    else:
        print("dia invalido")
elif mes==6:
    if 1<=dia<=21:
        print("geminis")
    elif 22<=dia<=30:
        print("cancer")
    else:
        print("dia invalido")
elif mes==7:
    if 1<=dia<=22:
        print("cancer")
    elif 23<=dia<=31:
        print("leo")
    else:
        print("dia invalido")
elif mes==8:
    if 1<=dia<=23:
        print("leo")
    elif 24<=dia<=31:
        print("virgo")
    else:
        print("dia invalido")
elif mes==9:
    if 1<=dia<=23:
        print("virgo")
    elif 24<=dia<=30:
        print("libra")
    else:
        print("dia invalido")
elif mes==10:
    if 1<=dia<=23:
        print("libra")
    elif 24<=dia<=31:
        print("escorpio")
    else:
        print("dia invalido")
elif mes==11:
    if 1<=dia<=22:
        print("escorpio")
    elif 23<=dia<=30:
        print("sagitario")
elif mes==12:
    if 1<=dia<=20:
        print("sagitario")
    elif 21<=dia<=31:
        print("capricornio")
    else:
        print("dia invalido")
else:
    print("mes invalido")
      