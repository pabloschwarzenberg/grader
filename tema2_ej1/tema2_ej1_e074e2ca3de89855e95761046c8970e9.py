def area_triangulo(base,altura):
    resultado = (base*altura)/2
    return resultado

def area_rectangulo(base,altura):
    resultado = base*altura
    return resultado

def area_rombo(diagonal1,diagonal2):
    resultado = (diagonal1 * diagonal2)/2
    return resultado

def area_circulo(radio):
    resultado = 3.141592653589793 * (radio**2)
    return resultado
    
if __name__ == "__main__":
  respuesta = input('Area que desea: ')
  if respuesta == 'triangulo':
    base = int(input('Base: '))
    altura = int(input('Altura: '))
    print(area_triangulo(base,altura))

  if respuesta == 'rectangulo':
    base = int(input('Base: '))
    altura = int(input('Altura: '))
    print(area_rectangulo(base,altura))

  if respuesta == 'rombo':
     diagonal1 = int(input('Diagonal 1: '))
     diagonal2 = int(input('Diagonal 2: '))
     print(area_rombo(diagonal1,diagonal2))

  if respuesta == 'circulo':
      radio = int(input('Radio: '))
      print(area_circulo(radio))