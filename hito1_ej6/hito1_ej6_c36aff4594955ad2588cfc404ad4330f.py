#Ordenar tres números
n1 = int(input("ingrese el primer numero: "))
n2 = int(input("ingrese el segundo numero: "))
n3 = int(input("ingrese el tercer numero: "))
mayor = 0
medio = 0
menor = n1
if ( n1 > mayor ):
    mayor = n1
if ( n2 > mayor ):
    mayor = n2
if ( n3 > mayor ):
    mayor = n3
if ( n2 < menor ):
    menor = n2
if ( n3 < menor ):
    menor = n3
medio = (n1 + n2 + n3) - (mayor + menor)
print ("el orden de menor a mayor es: " +str(menor)+", "+ str(medio)+", " + str(mayor)+".")