#Suma de los N primeros números
N = eval(input("Ingrese un número:"))
n = 1

for n in range(1,N+1):
    formula = ((n*(n+1))/2)
    n = n + 1
    print ("Las sumas son:",formula)