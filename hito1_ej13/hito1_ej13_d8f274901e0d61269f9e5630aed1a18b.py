#Factores Primos
#def (x)
#while range
#append

#Funcion para tener los factores primos
def factores(x):
    L = []

    for i in range(2, x+1):
        while x%i == 0:
            L.append(i)
            x = x / i
    return L

#Ingrese el número
y = int(input("Ingrese un número: "))
z =(factores(y))
#No se me ocurrio otra solucion bruuuuuuh
print(str(factores(y)[0]))
if len(z) > 1:
    print(str(factores(y)[1]))
if len(z) > 2:
    print(str(factores(y)[2]))
if len(z) > 3:
    print(str(factores(y)[3]))
if len(z) > 4:
    print(str(factores(y)[4]))
if len(z) > 5:
    print(str(factores(y)[5]))
if len(z) > 6:
    print(str(factores(y)[6]))
if len(z) > 7:
    print(str(factores(y)[7]))
if len(z) > 8:
    print(str(factores(y)[8]))
if len(z) > 9:
    print(str(factores(y)[9]))
if len(z) > 10:
    print(str(factores(y)[10]))
if len(z) > 11:
    print(str(factores(y)[11]))
if len(z) > 12:
    print(str(factores(y)[12]))