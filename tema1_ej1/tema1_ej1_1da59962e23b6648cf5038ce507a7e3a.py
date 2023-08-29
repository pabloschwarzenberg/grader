#Suma de los N primeros números
while True:
    n=int(input("Ingrese un número natural: "))
    if n>0:
        break
    else:
        print("Ingrese un número valido")
total=n*(n+1)/2
print(total)   