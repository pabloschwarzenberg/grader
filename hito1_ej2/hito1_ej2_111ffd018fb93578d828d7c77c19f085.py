#Contestador de celular
nf = int(input("ingrese el numero telefonico de 8 dígitos : "))
h = int(input("ingrese la hora de la llamada : "))
y = nf%1000
y2 = nf//100000
if h>=0 and h <=7:
    print("CONTESTAR")
elif h>7 and h<14:
        if y == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
elif 19>=h>=17:
            if y2 == 877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
elif 19<h<23:
             print("NO CONTESTAR")