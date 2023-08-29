#Contestador de celular
celular=int(input("Ingrese numero telefonico: "))
hora=int(input("Ingrese hora de la llamada: "))
if(0<=hora<=7):
    print("Resultado: CONTESTAR")
else:
    if(7<hora<14):
        if((celular%1000)==909):
            print("Resultado: CONTESTAR")
        else:
            print("Resultado: NO CONTESTAR")
    else:
        if(17<=hora<=19):
            if((celular//100000)==877):
                print("Resultado: NO CONTESTAR")
            else:
                print("Resultado: CONTESTAR")
        else:
            print("Resultado: NO CONTESTAR")
