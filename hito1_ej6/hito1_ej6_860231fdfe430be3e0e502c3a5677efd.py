#Ordenar tres números
x = int(input("Ingrese el primer número: "))
y = int(input("Ingrese el segundo número: "))
z = int(input("Ingrese el tercer número: "))

if((x <= y) and (x <= z)):
    
    menor = x

    if(y <= z):
        medio = y
        mayor = z
    else:
        medio = z
        mayor = y

elif((y <= z) and (y < z)):

    menor = y

    if(x <= z):
        medio = x
        mayor = z
    else:
        medio = z
        mayor = x

else:
    menor = z

    if(x <= y):
        medio = x
        mayor = y
    else:
        medio = y
        mayor = x
        
lista = [menor, medio, mayor]

print(lista)      