print("Ingrese 3 numeros: ")
a=int(input("ingrese 1° numero: "))
b=int(input("ingrese 2° numero: "))
c=int(input("ingrese 3° numero: "))

d=a, b, c
e=a, c, b
f=b, a, c
g=b, c, a
h=c, a, b
i=c, b, a

if a<=b<=c:
    print("El orden de los numeros de menor a mayor es el siguiente: ",d)
    
else:
    if a<=c<=b:
        print("El orden de los numeros de menor a mayor es el siguiente: ",e)

    else:
        if b<=a<=c:
            print("El orden de los numeros de menor a mayor es el siguiente: ",f)

        else:
            if b<=c<=a:
                print("El orden de los numeros de menor a mayor es el siguiente: ",g)

            else:
                if c<=a<=b:
                    print("El orden de los numeros de menor a mayor es el siguiente: ",h)

                else:
                    if c<=b<=a:
                        print("El orden de los numeros de menor a mayor es el siguiente: ",i)