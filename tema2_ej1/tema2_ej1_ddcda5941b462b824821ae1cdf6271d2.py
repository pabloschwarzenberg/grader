import math
def area_triangulo(base,altura):
    return (base*altura)/2

def area_rectangulo(base,altura):
    return base*altura

def area_rombo(diagonal1,diagonal2):
    return (diagonal1 * diagonal2)/2

def area_circulo(radio):
    return (radio * radio) * math.pi
if __name__ == "_main_":
  print("Calculadora geométrica \n 1 Calcular área del triangulo \n 2 Calcular área del rectangulo \n 3 Calcular área del rombo \n 4 Calcular área del circulo")
  valor_ingresado = 6
  while valor_ingresado != 0:
    valor_ingresado = int(input("Elija un valor"))
    if valor_ingresado == 1:
        print("Eligió calcular el área del Triangulo")
        base = int(input("Ingrese medidas de la base en numeros enteros: "))
        altura = int(input("Ingrese medidas de la altura en numeros enteros: "))
        print("El área seleccionada es: {}".format(area_triangulo(base,altura)))
    elif valor_ingresado ==2:
        print("Eligió calcular el área del Rectángulo")
        b = int(input("Ingrese medidas de la cara 1: "))
        a = int(input("Ingrese medidas de la cara 2: "))
        print("El área seleccionada es: {}".format(area_rectangulo(b,a)))
    elif valor_ingresado ==3:
        print("Eligió calcular el área del Rombo")
        d1 = int(input("Ingrese la Diagonal 1: "))
        d2 = int(input("Ingrese la Diagonal 2: "))
        print("El área seleccionada es: {}".format(area_rombo(d1,d2)))
    elif valor_ingresado ==4:
        print("Eligió calcular el área del Circulo")
        el_radio_es = int(input("Ingrese medidas del radio en numeros enteros: "))
        print("El área seleccionada es: {}".format(area_circulo(el_radio_es)))