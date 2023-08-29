from math import*

def area_triangulo(base,altura):
    area = base*altura/2
    return area

def area_rectangulo(base,altura):
    area = base*altura
    return area

def area_rombo(diagonal1,diagonal2):
    area = diagonal1*diagonal2/2
    return area

def area_circulo(radio):
    area = pi*radio**2
    return area
    
if __name__ == "__main__":
    figura = input("Ingresa el nombre de la figura con la que deseas trabajar:  ")
    while figura!="triangulo" and figura!="rombo" and figura!="circulo" and figura!="rectangulo":
        print("Lo siento, sólo puedes trabajar con un triangulo, rectangulo, circulo o rombo.")
        print("")
        figura = input("Ingresa el nombre de la figura con la que deseas trabajar:  ")

    if figura=="triangulo":
        base = float(input("Ingrese medida de la base: "))
        altura = float(input("Ingrese medida de la altura: "))
        print("")
        print("El área de tu triángulo es: ", area_triangulo(base, altura),"cm^2.")
               
    elif figura=="rectangulo":
        base = float(input("Ingrese medida del largo: "))
        altura = float(input("Ingrese medida del ancho: "))
        print("")
        print("El área de tu rectángulo es: ", area_rectangulo(base, altura),"cm^2.")
        
    elif figura=="circulo":
        radio = float(input("Ingrese medida del radio: "))
        print("")
        print("El área de tu círculo es: ", area_circulo(radio),"cm^2.")
        
    elif figura=="rombo":
        d = float(input("Ingrese medida de la diagonal menor: "))
        D = float(input("Ingrese medida de la diagonal mayor: "))
        print("")
        print("El área de tu rombo es: ", area_rombo(diagonal1, diagonal2),"cm^2.")    
          