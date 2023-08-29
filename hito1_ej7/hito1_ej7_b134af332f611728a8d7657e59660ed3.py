#Zodiaco
d=int(input())
m=int(input())

if (32>d>20 and m==3) or (d<21 and m==4):
    print("Aries")
elif (31>d>20 and m==4) or (0<d<22 and m==5):
    print("Tauro")
elif (32>d>21 and m==5) or (0<d<22 and m==6):
    print("geminis")
elif (31>d>21 and m==6) or (0<d<23 and m==7):
    print("Cancer")
elif (32>d>22 and m==7) or (0<d<23 and m==8):
    print("Leo")
elif (32>d>22 and m==8) or (0<d<24 and m==9):
    print("Virgo")
elif (31>d>23 and m==9) or (0<d<24 and m==10):
    print("Libra")
elif (32>d>23 and m==10) or (0<d>23 and m==11):
    print("Escorpión")
elif (31>d>22 and m==11) or (0<d<22 and m==12):
    print("Sagitario")
elif (32>d>21 and m==12) or (0<d<21 and m==1):
    print("Capricornio")
elif (32>d>22 and m==1) or (0<d<20 and m==2):
    print("Acuario")
elif (30>d>21 and m==2) or (0<d<21 and m==3):
    print("Piscis")