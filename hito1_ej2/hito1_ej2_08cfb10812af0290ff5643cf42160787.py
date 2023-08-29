#Contestador de celular
a=int(input("Ingrese numero telefonico: "))
b=int(input("Ingrese hora de la llamada: "))
c=a//100000
d=a/1000
e=abs(d)-abs(int(d))
f=e*1000
g=round(f,0)
h=abs(int(g))
if 0<b<7:
    print("CONTESTAR")
else:
    if 7<b<14 and h==909:
        print("CONTESTAR")
    else:
        if 7<b<14 and h!=909:
            print("NO CONTESTAR")
        else:
            if 14<b<17:
                print("NO CONTESTAR")
            else:
                if 17<b<19 and c==877:
                    print("NO CONTESTAR")
                else:
                    if 17<b<19 and c!=877:
                        print("CONTESTAR")
                    else:
                        print("NO CONTESTAR")