#Suma de los N primeros números

# utilizando la función N(N+1)/2
naturales = lambda n: int(n*(n+1)/2)
 
 
# utilizando un bucle recorriendo todos los valores y sumandolos
naturales = lambda n: sum([i for i in range(n+1)])

