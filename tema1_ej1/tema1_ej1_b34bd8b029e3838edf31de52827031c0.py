#Suma de los N primeros números
n= int(input("Ingrese un número entero positivo: "))
print(n)

if n < 1:
    print("El número debe ser un entero positivo.")
else:
    resutado=(n*(n+1)//2)
    
    print("La suma de los", n, "primeros números naturales es: ",resutado )      