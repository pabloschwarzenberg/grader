#Zodiaco
D=int(input("Ingresa el dia de tu cumpleaños: "))
M=int(input("Ingresa el mes de tu cumpleaños: "))
if (D>21 and M==3) or (D<20 and M==3):
    print("Aries")
if (D<21 and M==4) or (D<21 and M==5):
    print("Tauro")
if (D>22 and M==5) or (D<21 and M==6):
    print("Gemini")
if (D>22 and M==6) or (D<22 and M==7):
    print("Cancer")
if (D>23 and M==7) or (D<22 and M==8):
    print("Leo")
if (D>23 and M==8) or (D<23 and M==9):
    print("Virgo")
if (D>24 and M==8) or (D<23 and M==10):
    print("Libra")
if(D>24 and M==9) or (D<22 and M==11):
    print("Escorpion")
if (D>23 and M==11)or (D<21 and M==12):
    print("Sagitario")
if (D>22 and M==12)or (D<20 and M==1):
    print("Capricornio")
if (D>21 and M==1)or (D<19 and M==2):
    print("Acuario")
if (D>20 and M==2) or (D<20 and M==3):
    print("Piscis")

      