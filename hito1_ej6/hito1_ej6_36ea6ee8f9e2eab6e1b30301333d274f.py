#Ordenar tres números

#Ordenar tres numeros

a= int(input("ingresa el primer numero"))

b= int(input("ingresa el segundo numero"))

c= int(input("ingresa el tercer numero"))

q= max(a, b, c)

w= min(a, b, c)

e= (((a+b+c)-q)-w)

print("el orden de menor a mayor es:",w,",",e,",",q,)