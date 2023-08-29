#Contestador de celular

telefono = int(input("Telefono: "))
hora = int(input("Hora: "))

ulti = telefono%1000
#print(ulti_3)

prim = telefono // 100000
#print(3_prim)

ho_no = [15,16,20,21,22,23]

if hora in ho_no:
    print("Resultado: NO CONTESTAR")
else:
    if( hora >= 0 and hora <= 7):
        print("Resultado: CONTESTAR")
    elif( hora >= 8 and hora <= 14):
        if( ulti == 909 ):
            print("Resultado: CONTESTAR")
        else:
            print("Resultado: NO CONTESTAR")
    elif( hora >= 17 and hora <= 19):
        if( prim == 877 ):
           print("Resultado: NO CONTESTAR") 
        else:
            print("Resultado: CONTESTAR")
    else:
        print("Resultado: NO CONTESTAR")