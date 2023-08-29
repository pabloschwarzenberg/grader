import math

def calcular_area_rectangulo(base, altura):
    return base * altura

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    return (diagonal_mayor * diagonal_menor) / 2

def calcular_area_circulo(radio):
    return math.pi * radio**2

if __name__ == "__main__":
    def mostrar_menu():
        print("\nSelecciona una opción:")
        print("1. Calcular área de un rectángulo")
        print("2. Calcular área de un triángulo")
        print("3. Calcular área de un rombo")
        print("4. Calcular área de un círculo")
        print("5. Salir")
    
    def solicitar_parametros_rectangulo():
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        return base, altura
    
    def solicitar_parametros_triangulo():
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        return base, altura
    
    def solicitar_parametros_rombo():
        diagonal_mayor = float(input("Ingresa la longitud de la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingresa la longitud de la diagonal menor del rombo: "))
        return diagonal_mayor, diagonal_menor
    
    def solicitar_parametros_circulo():
        radio = float(input("Ingresa el radio del círculo: "))
        return radio
    
    print("¡Bienvenido! Este programa calcula el área de diferentes figuras geométricas.")
    
    while True:
        mostrar_menu()
        
        opcion = int(input("Ingresa el número de la opción deseada: "))
        
        if opcion == 1:
            base, altura = solicitar_parametros_rectangulo()
            area = calcular_area_rectangulo(base, altura)
            print(f"El área del rectángulo es: {area}")
        elif opcion == 2:
            base, altura = solicitar_parametros_triangulo()
            area = calcular_area_triangulo(base, altura)
            print(f"El área del triángulo es: {area}")
        elif opcion == 3:
            diagonal_mayor, diagonal_menor = solicitar_parametros_rombo()
            area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
            print(f"El área del rombo es: {area}")
        elif opcion == 4:
            radio = solicitar_parametros_circulo()
            area = calcular_area_circulo(radio)
            print(f"El área del círculo es: {area}")
        elif opcion == 5:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, selecciona una opción válida.")


