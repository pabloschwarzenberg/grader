#Contestador de celular
numTelefono = int(input("numero telefono:  "))
hora = int(input("ingrese hora de llamado:  "))
a = numTelefono%1000
b = numTelefono//100000

if hora >=0 and hora <= 7:
    print("CONTESTAR")
else:
    if hora>7 and hora<14:
        if a == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if 19>=hora>=17:
            if b == 877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        else:
            if 19<hora<23:
                print("NO CONTESTAR")