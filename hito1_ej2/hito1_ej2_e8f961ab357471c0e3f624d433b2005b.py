#Contestador de celular
n = int(input("ingrese el numero que contenga 8 digitos: "))
h = int(input("ingrese la hora del llamado: "))
tres_ulti = n%1000
tres_prim = n//100000
if((h>=0) and (h<=7)):
    print("CONTESTAR")
else:
    if((h>=13) and (tres_ulti == 909)):
        print("CONTESTAR")
    else:
        if((h>=17) and (h<=19) and (tres_prim == 877)):
            print("NO CONTESTAR")
        else:
            if(h>19):
                print("NO CONTESTAR")