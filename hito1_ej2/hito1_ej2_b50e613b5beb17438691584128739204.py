#Contestador de celular
numero=int(input("INGRESAR NUMERO TELEFONO:"))
hora=int(input("INGRESAR HORA DE LLAMADA:"))
texto = str(numero)


if hora>=0 and hora<=7:
    print("CONTESTAR")
    
elif hora>=8 and hora<=14:
    if "909" in texto:
        numerose=texto.index("909")
        if numerose ==5:
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    else:
        print("NO CONTESTAR")
elif hora>=17 and hora<=19:
    if "877" in texto:
                numerost = texto.index("877")
                if numerost==0:
                    print("NO CONTESTAR")
                else:
                    print("CONTESTAR")
    else:
        print("CONTESTAR")
elif hora>=3 and hora<=4:
    print("NO CONTESTAR")

elif hora>=19 and hora<=23:
    print("NO CONTESTAR")
     