# completa el código de la función
def suma_divisores(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    return suma

a = int(input("Ingresa el número: "))
salida=suma_divisores(a)

if salida==1:
  print("El numero no es primo")
else:
  print("El numero es primo")