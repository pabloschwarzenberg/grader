#Contestador de celular
n=int(input("ingrese 8 cifras"))
hora=int(input("ingrese una hora"))

if 10000000<= n <=99999999 and 0<= hora<=23:
    if 0<=hora==7:
        print("CONTESTAR")
    if hora>19:
        print("NO CONTESTAR")
    if hora<14:
        tresultimos=n%1000
        if tresultimos ==909:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    if 17<hora<=19:
        print("NO CONTESTAR")
    if 17<hora<=19:
        tresprimeros=n//100000
        if tresprimeros==877:
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")