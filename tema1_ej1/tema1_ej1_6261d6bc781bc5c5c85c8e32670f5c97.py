#EJERCICIO 2 H1-P1

N= int(input("Ingrese un número positIvo: "))
for n in range (N +1):
    sumannatural= (n)*(n+1)/2
    sumatotN= sumannatural+ N 
    print("El número natural",n,"Aplicado en la suma es= ",sumannatural,"\n")
print("La suma total de los",N,"primeros números naturales es: ", sumatotN)