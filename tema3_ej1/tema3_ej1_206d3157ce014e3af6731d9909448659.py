# completa el código de la función
print("Ingrese un numero: ")

a=int(input(" "))

def suma_divisores (a) :

    divisores = [1]

    

    for i in range (2, a+1):

        if a % i == 0:

            divisores.append(i)

            

    return sum(divisores)



resultado1 = suma_divisores(a)-a

print("La suma es: ",resultado1)



if resultado1 == a:

    print ("Numero Perfecto")

    print ("TRUE")

else:

    print ("No es numero Perfecto")

    print ("FALSE")

           