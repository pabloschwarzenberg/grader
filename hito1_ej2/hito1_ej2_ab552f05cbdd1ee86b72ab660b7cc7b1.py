#Contestador de celular
n=int(input("Ingrese numero telefonico: "))
h=int(input("ingrese hora de la llamada: "))
if h>=0 and h<=7:
    print("CONTESTAR")
if h>19 and h<=23:
    print("NO CONTESTAR")
if h>7 and h<14:
    if n%1000==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
if h>=14 and h<=19:
    if int(n/100000)==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
