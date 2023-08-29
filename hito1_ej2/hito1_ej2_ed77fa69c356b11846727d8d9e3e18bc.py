#Contestador de celular
n = int(input("Ingrese número de telefono:"))
h = int(input("Ingrese la hora:"))
n = str(n)

if 0 <= h <= 7:
    print("CONTESTAR")

else:
    if 7 < h <= 14:
        if int(n[5])==9 and int(n[6])==0 and int(n[7])==9:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")

    else:
        if 14 < h <= 17:
            print("NO CONTESTAR")
        else:
            if 17 < h <=19 and int(n[0])==8 and int(n[1])==7 and int(n[2])==7:
                print("NO CONTESTAR")
            else:
                print("CONTESTAR")
                if 19 < h <= 23:
                    print("NO CONTESTAR")
