#Contestador de celular
n = int(input("ingrese numero telefonico"))
h = int(input("ingrese hora de la llamada"))
nn = str(n)
ni = nn[0] + nn[1] + nn[2]
nu = nn[5] + nn[6] + nn[7]
if 0 <= h <= 7 :
    print("contestar")
else :
    if 7 < h <= 14 and nu == 909 :
        print("no contestar")
    else :
        if 17 < h < 19 and ni == 877 :
            print("no contestar")
        else :
            if h > 19 :
                print("no contestar")
            else :
                print("contestar")