import  math
def  area_rectangulo ( base , altura ):
    area = base  *  altura
def  area_triangulo ( baset , alturat ):
    area = ( baset  *  alturat ) /  2
def  area_rombo ( diagonal_mayor , diagonal_menor ):
    area = ( diagonal_mayor  *  diagonal_menor ) /  2
def  area_circulo ( radio ):
    a = math . pi  * ( radio  **  2 )
    print ( "1. Calcular area de un rectangulo" )
    print ( "2. Calcular area de un triangulo" )
    print ( "3. Calcular area de un rombo" )
    print ( "4. Calcular area de un circulo" )
    opción = int ( input ( "Selecciona una opción (1-4): " ))
    if opcion == 1:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        print("El área del rectángulo es:", area_rectangulo(base, altura))
    elif opcion == 2:
        baset = float(input("Ingresa la base del triángulo: "))
        alturat= float(input("Ingresa la altura del triángulo: "))
        print("El área del triángulo es:", area_triangulo(baset, alturat))
    elif opcion == 3:
        diagonal_mayor = float(input("Ingresa la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingresa la diagonal menor del rombo: "))
        print("El área del rombo es:", area_rombo(diagonal_mayor, diagonal_menor))
    elif opcion == 4:
        radio = float(input("Ingresa el radio del círculo: "))
        print("El área del círculo es:", area_circulo(radio))
    else:
        print("Opción inválida. Inténtalo de nuevo.")
