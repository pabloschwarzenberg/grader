#Contestador de celular
NT = int(input("ingrese el numero telefonico de 8 dígitos : "))
H = int(input("ingrese la hora de la llamada : "))
x = NT%1000
x2 = NT//100000
if H>=0 and H <=7:
    print("CONTESTAR")
elif H>7 and H<14:
        if x == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
elif 19>=H>=17:
            if x2 == 877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
elif 19<H<23:
             print("NO CONTESTAR")