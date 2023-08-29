d=int(input("Ingrese el día de su cumpleaños:"))
m=int(input("Ingrese el número del mes de su cumpleaños:"))
if 21<=d<=31 and m==3 or 1<=d<20 and m==4:
    print("Usted es Aries")
elif 20<=d<=30 and m==4 or 1<=d<21 and m==5:
    print("Usted es Tauro")
elif 21<=d<=31 and m==5 or 1<=d<21 and m==6:
    print("Usted es Geminis")
elif 21<=d<=30 and m==6 or 1<=d<23 and m==7:
    print("Usted es Cancer")
elif 23<=d<=31 and m==7 or 1<=d<23 and m==8:
    print("Usted es Leo")
elif 23<=d<=31 and m==8 or 1<=d<23 and m==9:
    print("Usted es Virgo")
elif 23<=d<=30 and m==9 or 1<=d<23 and m==10:
    print("Usted es Libra")
elif 23<=d<=30 and m==10 or 1<=d<22 and m==11:
    print("Usted es Escorpio")
elif 23<=d<=30 and m==11 or 1<=d<22 and m==12:
    print("Usted es Sagitario")
elif 22<=d<=30 and m==12 or 1<=d<20 and m==1:
    print("Usted es Capricornio")
elif 20<=d<=30 and m==1 or 1<=d<19 and m==2:
    print("Usted es Acuario")
elif 19<=d<=30 and m==2 or 1<=d<21 and m==3:
    print("Usted es Piscis")
else:
    print("Coloque un número viable por favor")