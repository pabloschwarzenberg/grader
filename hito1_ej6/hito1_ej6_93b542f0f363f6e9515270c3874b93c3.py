#Ordenar tres números
print("HOLA BUENAS, PORFAVOR INGRESAR SOLO NUMEROS ENTEROS.")
a= int(input("INGRESA UN NUMERO: "))
b= int(input("INGRESA UN NUMERO: "))
c= int(input("INGRESA UN NUMERO: "))

if a<b and a<c:
    menor=a
    if b<c:
        medio=b
        mayor=c
    else:
        medio=c
        mayor=b
elif b<a and b<c:
    menor=b
    if a<c:
        medio=a
        mayor=c
    else:
        medio=c
        mayor=a
elif c<b and c<a:
    menor=c
    if b<a:
        medio=b
        mayor=a
    else:
        medio=a
        mayor=b
print(menor,medio,mayor)
        
    

