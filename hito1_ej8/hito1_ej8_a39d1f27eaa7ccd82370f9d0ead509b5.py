numero=(input("ingresa un numero : "))
calculo=list(numero)

if len(calculo)<=4:
    if len (calculo) ==4:
        print(calculo[0]+"M","+",calculo[1]+"C","+",calculo[2]+"D","+",calculo[3]+"U")
    elif len (calculo) ==3:
        print (calculo[0] + "C","+", calculo[1] + "D","+", calculo[2] + "U")
    elif len (calculo) ==2:
        print (calculo[0] + "D","+", calculo[1] + "U", )
    elif len (calculo) ==1:
        print (calculo[0] + "U")
        

