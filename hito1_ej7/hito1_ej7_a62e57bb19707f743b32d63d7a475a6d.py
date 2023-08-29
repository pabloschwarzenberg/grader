#Programa Signos del Zodiaco
dia = int(input("Ingrese el día que nacio:  "))
mes = int(input("Indique en que mes nacio:  "))



if mes==1 and 20 <= dia <= 31 or mes==2 and 0 <= dia <=19:
    print("acuario")
elif mes==2 and 19 <= dia <=28 or mes==3 and 1 <= dia <=21:
    print("piscis")
elif mes==12 and 22 <= dia <= 30 or mes==1 and 1 <= dia <= 20:
    print("capricornio")
elif mes==11 and 23 <= dia <= 30 or mes==12 and 1 <= dia <= 22:
    print("sagitario")
elif mes==10 and 23 <= dia <= 30 or mes==11 and 1 <= dia <= 22:
    print("escorpio")
elif mes==9 and 23 <= dia <= 30 or mes==10 and 1 <= dia <= 23:
    print("libra")
elif mes==8 and 23 <= dia <= 30 or mes==9 and 1 <= dia <= 23:
    print("virgo")
elif mes ==7 and 23 <= dia <= 30 or mes==8 and 1<= dia <= 23:
    print("leo")
elif mes ==6 and 21 <= dia <= 30 or mes==7 and 1<= dia <= 23:
    print("cancer")
elif mes ==5 and 21 <= dia <= 30 or mes==6 and 1 <= dia <= 21:
    print("gemini")
elif mes ==4 and 20 <= dia <= 30 or mes==5 and 1 <= dia <= 21:
    print("taurus")
elif mes ==3 and 21 <= dia <= 30 or mes==4 and 1 <= dia <= 20:
    print("aries")
else:
    print("Invalido")
          
