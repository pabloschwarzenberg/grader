#Contestador de celular
n=int(input("Ingrese su número telefonico "))
while(n>99999999 or n<10000000):
    n=int(input("Ingrese su número telefonico "))
h=int(input("Ingrese la hora en la que está llamando "))
while(h>23 or h<0):
    h=int(input("Ingrese la hora en la que está llamando "))
if(h<=7 and h>=0):
    print("CONTESTAR")
else:
    if(h>7 and h<14):
        n1=n-909
        if ((n1%1000)==0):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if(h>=17 and h<=19):
            n2=n-87700000
            mate=round(n2/100000,-1)
            if(mate==0):
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        else:
            print("NO CONTESTAR")