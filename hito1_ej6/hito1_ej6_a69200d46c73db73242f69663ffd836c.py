#Ordenar tres números
a = int(input("Ingrese un numero entero al azar:  "))
b = int(input("Ingrese un numero entero al azar:  "))
c = int(input("Ingrese un numero entero al azar:  "))

#Transformación
if a <= b and a <= c and b <= c:
    menor = a , b , c
elif a <= b and a <= c and c <= b:
    menor = a , c , b
elif b <= a and b <= c and a <= c:
    menor = b , a , c
elif b <= a and b <= c and c <= a:
    menor = b , c , a
elif c <= a and c <= b and a <= b:
    menor = c , a , b
else:
    menor = c , b , a

#Entrega orden
print("El orden de los numeros de menor a mayor es" , menor)