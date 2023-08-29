#Ordenar tres números
a = int(input("Escriba el primer numero"))
b = int(input("Escriba el segundo numero"))
c = int(input("Escriba el tercer numero"))

if a > b:
    m = a
    m2 = b
    if m > c:
        mayor = m
        if m2 > c:
            medio = m2
            menor = c
        else:
            medio = c
            menor = m2
    else:
        mayor = c
        medio = m
        menor = m2
else:
    m = b
    m2 = a
    if m > c:
        mayor = m
        if m2 > c:
            medio = m2
            menor = c
        else:
            medio = c
            menor = m2
    else:
        mayor = c
        medio = m
        menor = m2
print(menor,",",medio,",",mayor)

    
       
 
       
       
       
       