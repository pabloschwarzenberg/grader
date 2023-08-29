#Contestador de celular
Numero = int(input("dame el numero:"))
hora = int(input("ingresa la hora: "))

variable1 = "contestar"
variable2 = "no contestar"
numeroprincipio = int(Numero / 100000)
numerofinal = Numero % 1000


if hora <= 24 and hora >= 0:

    if hora < 7:
        print ("resultado:", variable1)
    elif hora < 14 and hora >= 7 and numerofinal== 909:
        print ("resultado:", variable1)
    elif hora < 14 and hora >= 7:
        print ("resultado:", variable2)
    elif hora >= 14 and hora < 17 and numeroprincipio == 877:
        print ("resultado:", variable1)
    elif hora >= 17 and hora < 19 :
        print ("resultado:", variable2)
    elif hora >= 19 and hora < 24:
        print ("resultado:", variable2)
    else:
        print ("resultado:", variable2)

