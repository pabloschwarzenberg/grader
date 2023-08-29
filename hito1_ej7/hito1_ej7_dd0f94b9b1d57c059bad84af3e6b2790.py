#Zodiaco
dia=int(input("dia:"))
mes=int(input("mes:"))
if (mes==3 and 21<=dia) or (mes==4 and dia<20):
    print("Aries")
if (mes==4 and 20<=dia) or (mes==5 and dia<21):
    print("Tauro")
if (mes==5 and 21<=dia) or (mes==6 and dia<21):
    print("Gemini")
if (mes==6 and 21<=dia) or (mes==7 and dia<23):
    print("Cancer")
if (mes==7 and 23<=dia) or (mes==8 and dia<23):
    print("Leo")
if (mes==8 and 23<=dia) or (mes==9 and dia<23):
    print("Virgo")
if (mes==9 and 23<=dia) or (mes==10 and dia<23):
    print("Libra")
if (mes==10 and 23<=dia) or (mes==11 and dia<22):
    print("Escorpio")
if (mes==11 and 22<=dia) or (mes==12 and dia<22):
    print("Sagitario")
if (mes==12 and 22<=dia) or (mes==1 and dia<20):
    print("Capricornio")
if (mes==1 and 20<=dia) or (mes==2 and dia<19):
    print("Acuario")
if (mes==2 and 19<=dia) or (mes==3 and dia<21):
    print("Piscis")      