
a = int(input("Primer Numero: "))
b = int(input("Segundo Numero: "))
c = int(input("Tercer Numero: "))
menor,medio,mayor= 0,0,0
if a > b and a > c:
    mayor = a
    if b > c:
        medio, menor = b, c
    else:
        medio, menor = c, b
if b > a and b > c:
    mayor = b
    if a > c:
        medio, menor = a, c
    else:
        medio, menor = c, a
elif c > a and c > b:
    mayor = c
    if a > b:
        medio, menor = a, b
    else:
        medio, menor = b, a
elif a==b:
    if a==b:
       medio, menor= b,a
elif a==c:
    if a==c:
        menor,mayor,medio=b,a,c
        
       

print("El orden de los numeros son:", menor,",", medio,",", mayor)