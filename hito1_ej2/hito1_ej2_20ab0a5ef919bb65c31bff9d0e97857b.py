#Contestador de celular
telefono=int(input("Ingrese número de telefono: "))
hora=int(input("Ingrese la hora de la llamada :"))


if (hora>=0 and hora<=7):
    print("RESULTADO: CONTESTAR")
else:
    if( (hora < 14) and ( telefono%1000 ==909)):
        print("RESULTADO: CONTESTAR") 
    else:
        if(hora<14):
            print("RESULTADO: NO CONTESTAR")
        else:
            if( (hora >=17 and hora <=19) and (telefono//100000==877) ):
                print("RESULTADO: NO CONTESTAR")  
            else:
                if( (hora >=17 and hora <=19)):
                    print("RESULTADO: CONTESTAR")   
                else:
                    if(hora>19):
                        print("RESULTADO: NO CONTESTAR")    