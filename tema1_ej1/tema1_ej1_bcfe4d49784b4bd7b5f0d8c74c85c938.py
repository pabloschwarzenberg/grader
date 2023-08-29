#Suma de los N primeros números
n=int(input("Ingrese n: "))

num = lambda n: int(n*(n+1)/2)

print(num(n))