#Ordenar tres números
print("Ingrese tres números entero:")
a = int(input())
b = int(input())
c = int(input())

menor = min(a,b,c)
mayor = max(a,b,c)
medio = (a+b+c)-menor-mayor

print("Sus números ordenados de menor a mayor son:",menor,",",medio,",",mayor)