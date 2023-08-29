#Contestador de celular
numero = int(input("ingrese el numero :"))
hora = int(input(" ingrese la hora : "))

cambio = (numero % 1000)

if hora > 0 and hora < 7 :
    print (" CONTESTAR ")

elif hora < 14 :
    if cambio == 909 :
        print (" CONTESTAR ")
    else:
        print (" NO CONTESTAR")

elif hora > 17 and hora < 19 :
    c1 = int((numero % 1000000000) / 100000)
    if c1 == 877 :
        print ("NO CONTESTAR")
    else:
        print (" CONTESTAR")

elif hora > 19 :
    print (" NO CONTESTAR ")