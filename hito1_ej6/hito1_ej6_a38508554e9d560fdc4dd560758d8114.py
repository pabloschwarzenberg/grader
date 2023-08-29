n1 = int(input("bienvenido,ingrese el numero 1 :"))
n2 = int(input("bienvenido,ingrese el numero 2 :"))
n3 = int(input("bienvenido,ingrese el numero 3 :"))

if n1<=n2<=n3:
    print ("El orden de los numeros de menor a mayor es",n1,",",n2,",",n3)

elif n3<=n2<=n1:
    print ("El orden de los numeros de menor a mayor es",n3,",",n2,",",n1)
    
elif n2<=n3<=n1:
    print ("El orden de los numeros de menor a mayor es",n2,",",n3,",",n1)
    
elif n2<=n1<=n3:
    print ("El orden de los numeros de menor a mayor es",n2,",",n1,",",n3)
    
elif n1<=n3<=n2:
    print ("El orden de los numeros de menor a mayor es",n1,",",n3,",",n2)
    
elif n3<=n1<=n2:
    print ("El orden de los numeros de menor a mayor es",n3,",",n1,",",n2)            


    


      