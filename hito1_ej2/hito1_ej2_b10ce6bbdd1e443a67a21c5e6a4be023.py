#Contestador de celular
n = int(input("ingrese el numero telefonico al cual tienen que contestar:"))
hora = int(input("ingresa la hora de llamada:"))
x = n%1000
x2 = n//100000
if hora >=0 and hora <= 7:
    print("contestar")
else:
    if hora>7 and hora<14:
        if x == 909:
            print("contestar")
        else:
            print("no contestar")
    else:
        if 19>=hora>=17:
            if x2 == 877:
                print("no contestar")
            else:
                print("contestar")
        else:
            if 19<hora<23:
                print("no contestar")