#entrada

a= int(input("Escriba un numero entero:"))
b=int(input("Escriba un numero entero:"))
c=int(input("Escriba un numero entero:"))

#procesamiento

if (a < b) and (a < c):

    menor= a

    
    if(b < c):
            medio= b
            mayor= c
    else:
            medio = c
            mayor = b 

elif (b < a) and (b < c):

    menor= b

    if (a < c):

            medio= a
            mayor= c

    else:
            medio= c
            mayor= a



elif (c < a) and (c < b):

    menor= c

    if (a < b):

            medio= a
            mayor= b

    else:

            medio= b
            mayor= a


#salida

print("los numeros de menor a mayor son",menor, ",",medio, ",",mayor)




