from math import pi

if __name__ == "__main__":
    print("\n                MENU")
    print("")
    print("          1. ÁREA CÍRCULO")
    print("          2. ÁREA RECTÁNGULO")
    print("          3. ÁREA CUADRADO")
    print("          4. ÁREA TRIÁNGULO")
    print("          5. SALIR")
    print("")
    opcion = int(input("          Ingresa una opción: "))
    procesaOpciones(opcion)

def areaCirculo(radio):
    res = pi*radio**2
    return res
def areaRectangulo(largo, ancho):
    res = largo * ancho
    return res
def areaCuadrado(lado):
    res = lado**2
    return res
def areatriangulo(base, altura):
    res = (base * altura) / 2
    return res
def procesaOpciones(opcion):
    if opcion == 1:
        if __name__ == "__main__":
            radio = float(input("\n          Ingresa radio: "))
            area = areaCirculo(radio)
    elif opcion == 2:
        if __name__ == "__main__":
            largo = float(input("\n          Ingresa largo: "))
            ancho = float(input("\n          Ingresa ancho: "))
            areaRectangulo = areaRectangulo(largo, ancho)
    elif opcion == 3:
        if __name__ == "__main__":
            lado = float(input("\n          Ingresa lado: "))
            areaCuadrado = areaCuadrado(lado)
    elif opcion == 4:
        if __name__ == "__main__":    
            base = float(input("\n          Ingresa base: "))
            altura = float(input("\n          Ingresa altura: "))
            areaTriangulo = areatriangulo(base, altura)
    if opcion in [1, 2, 3, 4]:
        if __name__ == "__main__":    
            print("\n          El área es:", area)    