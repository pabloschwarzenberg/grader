n1 = int(input())
n2 = int(input())


if n1 > n2:
    maximo = n1
    minimo = n2
else:
    maximo = n2
    minimo = n1

n3 = int(input())

if n3 >= maximo:
    medio = maximo
    maximo = n3
elif n3 <= minimo:
    medio = minimo
    minimo = n3
else:
    medio = n3


print(str(minimo)+","+str(medio)+","+str(maximo))

