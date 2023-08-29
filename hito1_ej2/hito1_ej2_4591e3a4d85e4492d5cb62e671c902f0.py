#Contestador de celular
print("CONTESTADOR AUTOMATICO")
NRO =int(input("INGRESE NUMERO TELEFONICO (8 DIGITOS): "))
HORA = int(input("INGRESE HORA DE LLAMADA (ENTRE LAS 00 Y LAS 23): "))
if (NRO<0 or NRO>99999999):
    print("ERROR")
    print("EL NUMERO TELEFONICO NO ES VALIDO")
    print("POR FAVOR INGRESE UN NUMERO CON 8 DIGITOS")
elif HORA<0 or HORA>23:
    print("ERROR")
    print("LA HORA DE LLAMADA NO ES VALIDA")
    print("POR FAVOR INGRESE UNA HORA DE LLAMADA ENTRE LAS 00 Y LAS 23")
else:
    NRO=str(NRO)
    if HORA>=0 and HORA<=7:
        print("CONTESTAR")
    elif HORA>7 and HORA<14:
        if (NRO.find("9",5,6) and NRO.find("0",6,7) and NRO.find("9",7,8)):
            print("CONTESTAR")
        else:
            print("NO CONTESTAR")
    elif HORA>=14 and HORA<17:
        print("NO CONTESTAR")
    elif HORA>=17 and HORA<=19:
        if (NRO.find("8",5,6) and NRO.find("7",6,7) and NRO.find("7",7,8)):
            print("NO CONTESTAR")
        else:
            print("CONTESTAR")
    elif HORA>19:
        print("NO CONTESTAR")      