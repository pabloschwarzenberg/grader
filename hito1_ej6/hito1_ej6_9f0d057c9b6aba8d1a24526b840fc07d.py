numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))
numero3 = int(input("Ingrese el tercer número: "))
maximo, medio, minimo = 0, 0, 0
if numero1 >= numero2 and numero1 >= numero3 and numero2 <= numero3:
    maximo = numero1
    medio = numero3
    minimo = numero2
if numero1 >= numero2 and numero1 >= numero3 and numero3 <= numero2:
    maximo = numero1
    medio = numero2
    minimo = numero3
if numero2 >= numero1 and numero2 >= numero3 and numero3 <= numero1:
    maximo = numero2
    medio = numero1
    minimo = numero3
if numero2 >= numero1 and numero2 >= numero3 and numero1 <= numero3:
    maximo = numero2
    medio = numero3
    minimo = numero1
if numero3 >= numero2 and numero3 >= numero1 and numero1 <= numero2:
    maximo = numero3
    medio = numero2
    minimo = numero1
if numero3 >= numero2 and numero3 >= numero1 and numero1 <= numero2:
    maximo = numero3
    medio = numero2
    minimo = numero1
if numero3 >= numero2 and numero3 >= numero1 and numero1 <= numero2:
    maximo = numero3
    medio = numero2
    minimo = numero1
if numero3 >= numero2 and numero3 >= numero1 and numero2 <= numero1:
    maximo = numero3
    medio = numero1
    minimo = numero2

print(str(minimo) + "," + str(medio) + "," + str(maximo))
