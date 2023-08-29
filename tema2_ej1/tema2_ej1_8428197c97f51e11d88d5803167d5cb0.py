def area_triangulo(base,altura):
    pass

def area_rectangulo(base,altura):
    pass

def area_rombo(diagonal1,diagonal2):
    pass

def area_circulo(radio):
    pass

if __name__ == "__main__":
    pass
  print("¿Qué figura geométrica quieres calcular?")
    print("1. Rectángulo")
    print("2. Triángulo")
    print("3. Rombo")
    print("4. Círculo")

    opcion = int(input("Ingresa una opción: "))

    if opcion == 1:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        print(f"El área del rectángulo es {area_rectangulo(base, altura)}")
    elif opcion == 2:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        print(f"El área del triángulo es {area_triangulo(base, altura)}")
    elif opcion == 3:
        diagonal_mayor = float(input("Ingresa la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingresa la diagonal menor del rombo: "))
        print(f"El área del rombo es {area_rombo(diagonal_mayor, diagonal_menor)}")
    elif opcion == 4:
        radio = float(input("Ingresa el radio del círculo: "))
        print(f"El área del círculo es {area_circulo(radio)}")         