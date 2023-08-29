# completa el código de la función
def suma_divisores(a):
  suma_divisores = 0
  contador = 1
  primo = False
  while contador<a:
    if (a%contador) == 0:
      suma_divisores = suma_divisores + contador
    contador = contador + 1
  if suma_divisores == 1:
    primo = True
  return suma_divisores, primo
def area_triangulo(base,altura):
  area = basealtura/2
  return area

def area_rectangulo(base,altura):
  area = basealtura
  return area

def area_rombo(diagonal1,diagonal2):
  area = diagonal1diagonal2/2
  return area

def area_circulo(radio):
  area = 3.141592653589793 * radio * radio
  return area 

def numero_perfecto(a):
  suma_divisores = 0
  contador = 1
  perfecto = False

  while contador < a:
    if (a % contador) == 0:
      suma_divisores = suma_divisores + contador
    contador = contador + 1 

  if suma_divisores == a:
    perfecto = True

  return perfecto
           