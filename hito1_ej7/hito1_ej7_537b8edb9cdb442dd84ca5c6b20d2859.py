dia_de_nacimiento=input("dia de nacimiento: ")
dia_de_nacimiento=int(dia_de_nacimiento)
mes_nacimiento=input("mes de nacimiento: ")
mes_nacimiento=int(mes_nacimiento)
if dia_de_nacimiento>21 and mes_nacimiento==3 or dia_de_nacimiento<20 and mes_nacimiento==4:
    print("aries")
if dia_de_nacimiento>21 and mes_nacimiento==4 or dia_de_nacimiento<21 and mes_nacimiento==5:
    print("tauro")
if dia_de_nacimiento>22 and mes_nacimiento==5 or dia_de_nacimiento<21 and mes_nacimiento==6:
    print("geminis")
if dia_de_nacimiento>22 and mes_nacimiento==5 or dia_de_nacimiento<22 and mes_nacimiento==7:
    print("Cancer")
if dia_de_nacimiento>23 and mes_nacimiento==7 or dia_de_nacimiento<22 and mes_nacimiento==8:
    print("Leo")
if dia_de_nacimiento>23 and mes_nacimiento==8 or dia_de_nacimiento<23 and mes_nacimiento==9:
    print("Virgo")
if dia_de_nacimiento>24 and mes_nacimiento==9 or dia_de_nacimiento<23 and mes_nacimiento==10:
    print("libra")
if dia_de_nacimiento>24 and mes_nacimiento==10 or dia_de_nacimiento<22 and mes_nacimiento==11:
    print("escorpio")
if dia_de_nacimiento>23 and mes_nacimiento==11 or dia_de_nacimiento<21 and mes_nacimiento==12:
    print("sagitario")
if dia_de_nacimiento>22 and mes_nacimiento==12 or dia_de_nacimiento<20 and mes_nacimiento==1:
    print("capricornio")
if dia_de_nacimiento>21 and mes_nacimiento==1 or dia_de_nacimiento<19 and mes_nacimiento==2:
    print("Aquarius")
if dia_de_nacimiento>21 and mes_nacimiento==2 or dia_de_nacimiento<20 and mes_nacimiento==3:
    print("piscis")