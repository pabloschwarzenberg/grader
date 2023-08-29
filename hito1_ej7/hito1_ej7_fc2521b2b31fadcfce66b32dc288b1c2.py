#Zodiaco
dia=input("dia de nacimiento:")
mes=input("mes de nacimiento:")
dia=int(mes)
mes=int(mes)
if mes==1 and 19<dia or(mes==2 and 0<dia and 19>dia):
    print("acuario")
elif mes==2 and dia>18 or(mes==3 and 0<dia and 21>dia):
    print("Piscis")
elif mes==3 and dia>20 or(mes==4 and 0<dia and 20>dia):
    print("Aries")
elif mes==4 and dia>19 or(mes==5 and 0<dia and 21>dia):
    print("Tauro")
elif mes==5 and dia>20 or(mes==6 and 0<dia and 21>dia):
    print("Geminis")
elif mes==6 and dia>20 or(mes==7 and 0<dia and 23>dia):
    print("Cancer")
elif mes==7 and dia>22 or(mes==8 and 0<dia and 23>dia):
    print("Leo")
elif mes==8 and dia>22 or(mes==9 and 0<dia and 23>dia):
    print("Virgo")
elif mes==9 and dia>22 or(mes==10 and 0<dia<23):
    print("Libra")
elif mes==10 and dia>22 or(mes==11 and 0<dia and 22>dia):
    print("escorpio")
elif mes==11 and dia>21 or(mes==12 and 0<dia and 22>dia):
    print("Sagitario")
elif mes==12 and dia>21 or(mes==1 and 0<dia and 20>dia):
    print("Capricornio")
    
    