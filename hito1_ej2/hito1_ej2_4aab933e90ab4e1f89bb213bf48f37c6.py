#Contestador de celular
l = int(input("ingrese su numero telefonico:"))
h = eval(input("ingrese la hora de su llamada:"))
if 100000000>l >9999999 and 7>=h>=0:
    print("CONTESTAR")
else:
    if 100000000>l >9999999 and (14>h>7) and ((l % 1000)== 909):
        print("CONTESTAR")
    else:
        if 100000000>l >9999999 and 19>=h>=17 and int(l / 100000)!=877:
            print("CONTESTAR")    
        else:
            print("NO CONTESTAR")
