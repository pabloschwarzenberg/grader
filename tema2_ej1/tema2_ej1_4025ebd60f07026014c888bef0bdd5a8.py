def areaTriangulo():
  Base = int(input("Ingrese valor: "))
  Altura = int(input("Ingrese valor: "))
  Area = (Base * Altura)/2
  print(Area)
def areaRectangulo():
  Base = int(input("Ingrese valor: "))
  Altura = int(input("Ingrese valor: "))
  Area = (Base * Altura)
  print(Area)

def areaRombo():
  Diagonal1 = int(input("Ingrese valor: "))
  Diagonal2 = int(input("Ingrese valor: "))
  Area = (Diagonal1 * Diagonal2)/2
  print(Area)

def areaCirculo():
  pi = 3.14
  Radio = int(input("Ingrese valor: "))
  Area = (pi * Radio ** 2)
  print(Area)
  

def salir():
  print("Gracias por usar la calculadora")
  
def menu():
  op = 0
  op = int(input("Digite su opcion a calcular: "))
  while op != 5:
    print("1.- Area_triangulo")
    print("2.- Area_rectangulo")
    print("3.- Area_rombo")
    print("4.- Area_circulo")
    print("5.- Salir")
    

    if op == 1:
        areaTriangulo()
    elif op == 2:
        areaRectangulo()
    elif op == 3:
        areaRombo()
    elif op == 4:
        areaCirculo()
    elif op == 5:
        salir()

menu()
