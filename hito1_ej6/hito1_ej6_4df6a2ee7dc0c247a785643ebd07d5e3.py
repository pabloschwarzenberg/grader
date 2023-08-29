numero1 = int(input("hola,ingrese el numero 1 :"))
numero2 = int(input("hola,ingrese el numero 2 :"))
numero3 = int(input("hola,ingrese el numero 3 :"))

if numero1<=numero2<=numero3:
    print ("El orden de los numeros de menor a mayor es",numero1,",",numero2,",",numero3)
elif numero1<=numero3<=numero2:
    print ("El orden de los numeros de menor a mayor es",numero1,",",numero3,",",numero2)
    
elif numero3<=numero2<=numero1:
    print ("El orden de los numeros de menor a mayor es",numero3,",",numero2,",",numero1)

elif numero2<=numero1<=numero3:
    print ("El orden de los numeros de menor a mayor es",numero2,",",numero1,",",numero3)
elif numero3<=numero1<=numero2:
    print ("El orden de los numeros de menor a mayor es",numero3,",",numero1,",",numero2) 
    
elif numero2<=numero3<=numero1:
    print ("El orden de los numeros de menor a mayor es",numero2,",",numero3,",",numero1)