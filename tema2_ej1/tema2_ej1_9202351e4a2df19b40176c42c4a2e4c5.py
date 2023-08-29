def main():
    choice = '0'
    while choice !='5':
        print("Opciones:")
        print("1.- Área Triangulo")
        print("2.- Área Rectangulo")
        print("3.- Área Rombo")
        print("4.- Área Circulo")
        print("5.- Salir")

        choice = input ("Ingresar opción: ")

        if choice == "1":
                base = int(input ("Ingresar base: "))
                altura = int(input ("Ingresar altura: "))
                area_triangulo(base,altura)

        elif choice == "2":
                base = int(input ("Ingresar base: "))
                altura = int(input ("Ingresar altura: "))
                area_rectangulo(base,altura)

        elif choice == "3":
                diagonal1 = int(input ("Ingresar diagonal1: "))
                diagonal2 = int(input ("Ingresar diagonal2: "))
                area_rombo(diagonal1,diagonal2)
        elif choice == "4":
                radio = int(input ("Ingresar radio: "))
                area_circulo(radio)
        elif choice == "5":
             print("Ha salido exitosamente")
        else:
            print("No se encuentra dentro de la opciones")

def area_triangulo(base,altura):
    resultado = (base*altura)/2
    print("El area de un triangulo de base ",base, 'y altura', altura 'es de ', resultado)
    

def area_rectangulo(base,altura):
  resultado = base*altura
  print("El area de un rectangulo de lados ",base, 'y',altura, 'debiera ser', resultado)
  

def area_rombo(diagonal1,diagonal2):
  resultado = (diagonal1*diagonal2)/2
  print("El area de un rombo con diagonales", diagonal1, 'y', diagonal2, 'debiera ser', resultado)
  

def area_circulo(radio):
  resultado =3.141516 * radio ** 2
  print("El area de un círculo de radio", radio, 'deberia ser', resultado)
  

if __name__ == "__main__":