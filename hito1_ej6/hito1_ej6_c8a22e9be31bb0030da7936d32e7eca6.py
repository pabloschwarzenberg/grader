#Ordenar tres números
X= int(input("escriba el primer numero: "))

Y= int(input("escriba el segundo numero: "))

Z= int(input("escriba el tercer numero: "))



a=min(X,Y,Z)

c=max(X,Y,Z)

b=(X+Y+Z)-a-c

print("los numeros ordenados son: {}, {}, {}".format(a, b, c))


