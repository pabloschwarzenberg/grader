#Contestador de celular
num_ = int(input("Ingrese el numero telefonico que lo esta llamando:"))
hora_ = int(input("Ingrese la hora que lo estan llamando:"))

x = num_%1000
x2 = num_//100000

if hora_ >=0 and hora_ <= 7:
    print("CONTESTAR")
else:
    if hora_>7 and hora_<14:
        if x == 909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        if 19>=hora_>=17:
            if x2 == 877:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
        else:
            if 19<hora_<23:
                print("NO CONTESTAR")
      