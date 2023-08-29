#Contestador de celularfono=int(input("NUMERO DE TELEFONO 8 DIGITOS: "))
fono=int(input("INGRESE NUMERO TELEFONICA 8 DIGITOS: "))
hora=int(input("SELECCIONAR HORA DE LLAMADA, 00 A 23: "))
exep1=fono%1000
exep2=int((fono%100000000)/100000)
if hora>=00 and hora<=7:
    print("CONTESTAR")

if hora>7 and hora<14:
    if exep1==909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")
    
if hora>=17 and hora<=19:
    if exep2==877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")
    
if hora>19 and hora<=23:
    print ("NO CONTESTAR")

      