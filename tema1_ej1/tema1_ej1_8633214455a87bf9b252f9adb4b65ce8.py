#Suma de los N primeros números
n = int(input("ingrese un número: "))

i = 0

j = 0

while j <= n:
    i += j

    j += 1

    print("variable i: ", i, "variable j: ", j)

print("La suma de los numero de %d es: %d" % (n, i))      