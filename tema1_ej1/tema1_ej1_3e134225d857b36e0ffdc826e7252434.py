#Suma de los N primeros números
n=int(input("ingresar numero: "))
naturales = lambda n: int(n*(n+1)/2)

for i in range(1,n + 1):
    print(i)
    
print(naturales (n))     