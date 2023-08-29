#Entrada
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))

#Procesamiento

if a <= b and a <= c:
    menor = a
    if b <= c:
        medio = b
        mayor = c
    else:
        medio = c
        mayor = c
elif b <= a and b <= c:
    menor = b
    if a <= c:
        medio = a
        mayor = c
    else:
        medio = c
        mayor = a
elif c <= a and c<= b:
    menor = c
    if a <= b:
        medio = a
        mayor = b
    else:
        medio = b
        mayor = a
#salida
        
print("Los números ordenados de menor a mayor son: ", menor,str(","), medio,str(","), mayor)
     
      