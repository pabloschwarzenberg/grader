#Descomponer un número
mil = int(0)
centena = int(0)
decena = int(0)
unidad = int(0)
numero = int(input("Ingrese valor no superior a 4 digitos -> "))
if numero < 10000:
    if ((numero>=0) and (numero<10)):
        print(numero,"U")
        
    elif numero >=10 and numero < 100:
        decena = int(numero / 10) 
        unidad = int(numero - (decena *10))
        print(decena,"D +",unidad,"U")
        
    elif numero >= 100 and numero < 1000:
        centena = int(numero / 100)
        decena = int((numero - (centena * 100)) / 10)
        unidad = int(numero - (centena * 100) - (decena * 10))
        print(centena,"C +",decena,"D +",unidad,"U")
        
    else:
        mil = int(numero / 1000)
        centena = int((numero - (mil * 1000)) / 100)
        decena = int((numero - (centena * 100) - (mil * 1000)) / 10)
        unidad = int(numero - (mil * 1000) - (centena * 100) - (decena * 10))
        print(mil,"M +",centena,"C +",decena,"D +",unidad,"U")

else:
    print("Debe ingresar un numero menor a 10000")     