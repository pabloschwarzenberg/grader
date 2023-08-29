#Suma de los N primeros números
while True:
    try:
        n = int(input("Escriba el numero natural: "))

        if n > 1:
            break
        else:
            print("Debe ingresar un numero entero positivo")
    except ValueError:
        print("Debe escribir un numero estero valido")

    print()

suma = n * (n + 1) / 2
print(suma)

print()

print(sum(range(1, n+1)))