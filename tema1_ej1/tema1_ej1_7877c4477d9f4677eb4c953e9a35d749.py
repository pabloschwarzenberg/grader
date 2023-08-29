#Suma de los N primeros números

n = int(input("Número natural diferente de 0:"))
while not(n>0):
    n = int(input("Natural y diferente de 0 >,>):"))
Plus = n*(n + 1)/2
print("La suma de los primer", n," números es:", Plus)