n1 = int(input("escriba aquí un numero: "))
n2 = int(input("escriba aquí un numero: "))
n3 = int(input("escriba aquí un numero: "))
      
#Operaciones.

if n1 <= n2 <= n3:
    print("el orden de menor a mayor es",n1,",",n2,",",n3)
elif n1 <= n3 <= n2:
    print("el orden de menor a mayor es",n1,",",n3,",",n2)
elif n2 <= n1 <= n3:
    print("el orden de menor a mayor es",n2,",",n1,",",n3)
elif n2 <= n3 <= n1:
    print("el orden de menor a mayor es",n2,",",n3,",",n1)
elif n3 <= n1 <= n2:
    print("el orden de menor a mayor es",n3,",",n1,",",n2)
else:
    print("el orden de menor a mayor es",n3,",",n2,",",n1)