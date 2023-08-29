#Ordenar tres números
print("Te ordeno tus numeros de menor a mayor")
x=int(input("Dame el primer numero"))
            
y=int(input("Dame el segundo numero"))
             
z=int(input("Dame el tercer numero"))

a=min(x, y, z)

c=max(x, y, z)

b=(x+y+z)-a-c

print("Tus numeros ordenados son: {}, {}, {}".format(a, b, c))