#Zodiaco
def obtener_signo(dia_nacimiento,mes_nacimiento):
    signo = ""
    if mes_nacimiento == 1:
        if dia_nacimiento <= 20:
            print ("capricornio")
        else:
            print ("acuario")
    elif mes_nacimiento == 2:
        if dia_nacimiento <= 18:
            print ("acuario")
        else:
            print ("picis")
    elif mes_nacimiento == 3:
        if dia_nacimiento <= 20:
            print ("picis")
        else:
            print ("aries")
    elif mes_nacimiento == 4:
        if dia_nacimiento <= 20:
            print ("aries")
        else:
            print ("tauro")
    elif mes_nacimiento == 5:
        if dia_nacimiento <= 21:
            print ("Tauro")
        else:
            print ("geminis")
    elif mes_nacimiento == 6:
        if dia_nacimiento <= 21:
            print ("geminis")
        else:
            print ("cancer")
    elif mes_nacimiento == 7:
        if dia_nacimiento <= 22:
            print ("cancer")
        else:
            print ("leo")
    elif mes_nacimiento == 8:
        if dia_nacimiento <= 23:
            print ("leo")
        else:
            print ("virgo")
    elif mes_nacimiento == 9:
        if dia_nacimiento <= 23:
            print ("virgo")
        else:
            print ("libra")
    elif mes_nacimiento == 10:
        if dia_nacimiento <= 23:
            print ("libra")
        else:
            print ("escorpio")
    elif mes_nacimiento == 11:
        if dia_nacimiento <= 22:
            print ("Escorpio")
        else:
            print ("sagitario")
    elif mes_nacimiento == 12:
        if dia_nacimiento <= 21:
            print ("sagitario")
        else:
            print ("capricornio")
    return signo
dia_nacimiento=int(input())
mes_nacimiento=int(input())
obtener_signo(dia_nacimiento,mes_nacimiento)