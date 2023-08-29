#Ordenar tres números

a = int(input("Ingrese un número: "))
b = int(input("Ingrese un número: "))
c = int(input("Ingrese un número: "))

if a > c:
    a = a + c
    c = a - c
    a = a - c  
if a > b:
    a = a + b
    b = a - b
    a = a - b
if b > c:
    b = b + c
    c = b - c
    b = b - c
print("{},{},{}".format(a,b,c))