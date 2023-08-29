#Ordenar tres números


#pido al usuario que ingrese los numeros
numero_1 = int(input("ingrese el primer numero: "))
numero_2 = int(input("ingrese el segundo numero: "))
numero_3 = int(input("ingrese el tercer numero: "))
#declaro variables de mayor, medio y menor
mayor = 0
medio = 0
menor = 0

#si numero_1 es el mayor
if numero_1 > numero_2 and numero_1 > numero_3:
    mayor = numero_1
    #si numero_2 es mayor que numero_3
    if numero_2 > numero_3:
        medio = numero_2
        menor = numero_3
    #si numero_3 es mayor que numero_2
    else:
        medio = numero_3
        menor = numero_2

#si numero_2 es el mayor
if numero_2 > numero_1 and numero_2 > numero_3:
    mayor = numero_2
    #si numero_1 es mayor que numero_3
    if numero_1 > numero_3:
        medio = numero_1
        menor = numero_3
    #si numero_3 es mayor que numero_1
    else:
        medio = numero_3
        menor = numero_1

#si numero_3 es el mayor
if numero_3 > numero_1 and numero_3 > numero_2:
    mayor = numero_3
    #si numero_1 es mayor que numero_2
    if numero_1 > numero_2:
        medio = numero_1
        menor = numero_2
    #si numero_2 es mayor que numero_1
    else:
        medio = numero_2
        menor = numero_1

#si numero_1 y numero_2 son iguales pero numero_3 es menor        
if numero_1 == numero_2 > numero_3:
    mayor = numero_1
    medio = numero_2
    menor = numero_3

#si numero_1 y numero_2 son iguales pero numero_3 es mayor        
if numero_1 == numero_2 < numero_3:
    mayor = numero_3
    medio = numero_2
    menor = numero_1

#si numero_3 y numero_2 son iguales pero numero_1 es menor        
if numero_3 == numero_2 > numero_1:
    mayor = numero_3
    medio = numero_2
    menor = numero_1

#si numero_3 y numero_2 son iguales pero numero_1 es mayor        
if numero_3 == numero_2 < numero_1:
    mayor = numero_1
    medio = numero_2
    menor = numero_3

#si numero_3 y numero_2 son iguales pero numero_2 es menor        
if numero_3 == numero_1 > numero_2:
    mayor = numero_3
    medio = numero_1
    menor = numero_2

#si numero_3 y numero_2 son iguales pero numero_2 es mayor        
if numero_3 == numero_1 < numero_2:
    mayor = numero_2
    medio = numero_1
    menor = numero_3

#si todos los numeros son iguales
if numero_3 == numero_2 == numero_1:
    mayor = numero_3
    medio = numero_2
    menor = numero_1

print(menor, "," , medio, "," , mayor)