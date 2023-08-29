#Ordenar tres numeros
#Entradas
a = int(input("Ingrese el primer numero: "))
b = int(input("Ingrese el segundo numero: "))
c = int(input("Ingrese el tercer numero: "))
#Procedimiento
if a >= b and a >= c:
    mayor = a
    if b > c:
        medio = b
    else:
        medio = c
elif b >= a and b >= c:
    mayor = b
    if a > c:
        medio = a
    else:
        medio = c 
elif c >= a and c >= b:
    mayor = c
    if a > b:
        medio = a
    else:
        medio = b

if a <= b and a <= c:
    menor = a
elif b <= a and b <= c:
    menor = b
else:
    menor = c


#Salidas
print (menor,",",medio,",",mayor)

