x = int(2) 
numeroP = int(input("Ingrese el numero: ")) 
while(numeroP != 1): 
  if (numeroP % x == 0 ):
    print(str(x) + "") 
    numeroP = numeroP / x 
  else:
    x = x + 1


# suma de los divisores de un numero

def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    if suma == 1:
        return suma, True  # Retorna la suma y True si el número es primo
    else:
        return suma, False  # Retorna la suma y False si el número no es primo

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    suma, es_primo = suma_divisores(numero)
    print("Suma de los divisores:", suma)
    print("¿Es primo?", es_primo)

# calculadora geometrica

import math

def area_rectangulo(base, altura):
    return base * altura

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    print("¡Bienvenido al programa de cálculo de áreas!")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")
    opcion = int(input("Seleccione una figura (1-4): "))

    if opcion == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        resultado = area_rectangulo(base, altura)
        print("El área del rectángulo es:", resultado)
    elif opcion == 2:
        base = float(input("Ingrese la base del triángulo: "))
        altura = float(input("Ingrese la altura del triángulo: "))
        resultado = area_triangulo(base, altura)
        print("El área del triángulo es:", resultado)
    elif opcion == 3:
        diagonal_mayor = float(input("Ingrese la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingrese la diagonal menor del rombo: "))
        resultado = area_rombo(diagonal_mayor, diagonal_menor)
        print("El área del rombo es:", resultado)
    elif opcion == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        resultado = area_circulo(radio)
        print("El área del círculo es:", resultado)
    else:
        print("Opción inválida. Por favor, seleccione una opción válida (1-4).")