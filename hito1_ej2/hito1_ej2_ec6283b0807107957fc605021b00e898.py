#Contestador de celular
nt=int(input("Ingrese su número telefonico "))
while(nt>99999999 or nt<10000000):
    nt=int(input("Ingrese su número telefonico "))
hl=int(input("Ingrese la hora en la que está llamando "))
while(hl>23 or hl<0):
    hl=int(input("Ingrese la hora en la que está llamando "))
if(hl<=7 and hl>=0):
    print("CONTESTAR")
else:
    if(hl>7 and hl<14):
        n1=nt-909
        if ((n1%1000)==0):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if(hl>=17 and hl<=19):
            nt2=nt-87700000
            mate=round(nt2/100000,-1)
            if(mate==0):
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        else:
            print("NO CONTESTAR")