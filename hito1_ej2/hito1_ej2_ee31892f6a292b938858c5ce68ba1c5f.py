#Contestador de celular
telefono =int(input("Ingresa el numero telefonico: "))
hora =int(input("Ingresa hora de la llamada: "))


if 10000000<= telefono <=99999999 and hora<=23:
    
    if 0<=hora<=7:
        print("RESULTADO: CONTESTAR")
        
    if 8<=hora<=14:
        tresultimosdigitos= telefono%1000
        if tresultimosdigitos== 909:
            print("RESULTADO: CONTESTAR")

        else:
            print("RESULTADO: NO CONTESTAR")

    if 15<=hora<=16:
        print("RESULTADO: NO CONTESTAR")

    if 17<=hora<=19:
        tresprimerosdigitos= telefono//100000
        if tresprimerosdigitos== 877:
            print("RESULTADO: NO CONTESTAR")
            
        else:
            print("RESULTADO: CONTESTAR")

    if 20<=hora<=23:
        print("RESULTADO: NO CONTESTAR")
               
else:
    print("Uno o mas de los datos ingresados no son validos")     