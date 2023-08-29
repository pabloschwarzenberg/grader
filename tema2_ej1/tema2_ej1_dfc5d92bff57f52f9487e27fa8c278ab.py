from math import pi

def area_triangulo(base,altura):
    area_t = (base * altura) / 2
    return(area_t)

def area_rectangulo(base,altura):
    area_rec = (base * altura)
    return(area_rec)

def area_rombo(diagonal1,diagonal2):
    area_rom = (diagonal1 * diagonal2) / 2
    return(area_rom)

def area_circulo(radio):
    area_c = (radio ** 2) * pi
    return(area_c)


if __name__ == "__main__":
  print('--------------------------------------------------------------------------------\n'
        'Ingrese a continuación cuál de las siguientes opciones desea obtener el área\n'
        '(Se necesita que ud ingrese ciertos datos para calcular)\n'
        '--------------------------------------------------------------------------------\n'
        '                               - Triángulo\n'
        '                               (Área y base)\n\n'
        
        '                               - Rectángulo\n'
        '                               (Área y base)\n\n'
        
        '                                 - Rombo\n'
        '                          (Diagonal 1 y diagonal 2)\n\n'
        
        '                                - Círculo\n'
        '                                  (Radio)\n'
        '--------------------------------------------------------------------------------')

  while True:
      eleccion = input('Ingrese la figura que necesite calcular: ')
      if eleccion in('Triángulo','triángulo','Triangulo','triangulo'):
          base_t = int(input('\nIngrese la medida de la base de su triángulo: '))
          altura_t = int(input('Ingrese la medida de la altura de su triángulo: '))
          area_triangulo(base_t, altura_t)
      elif eleccion in('Rectángulo','rectángulo','Rectangulo','rectangulo'):
          base_rec = int(input('\nIngrese la medida de la base de su rectángulo: '))
          altura_rec = int(input('Ingrese la medida de la altura de su rectángulo: '))
          area_rectangulo(base_rec,altura_rec)
      elif eleccion in('Rombo','rombo',):
          diagonal_1 = int(input('\nIngrese la medida de la 1ra diagonal de su rombo: '))
          diagonal_2 = int(input('Ingrese la medida de la 2da diagonal de su rombo: '))
          area_rombo(diagonal_1,diagonal_2)
      elif eleccion in('Círculo','círculo','Circulo','circulo'):
          r = int(input('\nIngrese el radio de su círculo: '))
          area_circulo(r)
      orden = input("Desea realizar otra operación?: ")
      if orden in ("si", "Si"):
          continue
      elif orden in ('no', 'No'):
          print('\nUsted ha decidido salir')
          break
      break