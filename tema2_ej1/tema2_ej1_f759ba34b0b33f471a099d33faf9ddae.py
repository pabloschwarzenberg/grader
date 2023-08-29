import math
def area_triangulo(base1,altura1):
    area = (int (base1) *  int (altura1)) / 2.0

def area_rectangulo(base2,altura2):
    area2=base2*altura2

def area_rombo(diagonal1,diagonal2):
    area=(diagonal1*diagonal2)/2

def area_circulo(radio):
   a = math.pi* (radio*radio)

if __name__ == "__main__":
    print("¿Que operación matemática desea realizar?")
    print("Opcion 1. Area Triangulo")
    print("Opcion 2. Area Rectangulo")
    print("Opcion 3. Area Rombo")
    print("Opcion 4. Area Circulo")
    print("Opcion 0. SALIR")
    op = eval(input("Ingrese una opcion: "))
    print("Ha escogido la Area Triangulo")
    print("Ha escogido la operacion Area Rectangulo")
    print("Ha escogido la operacion Area Rombo")
    print("Ha escogido la operacion Area Circulo")
    base1=input("CUAL ES LA BASE DEL TRIANGULO: ")
    altura1=input("CUAL ES LA ALTURA DEL TRIANGULO: ")
    base2=float(input("ingrese ancho de rectangulo\n"))
    altura2=float(input("ingrese alto de rectangulo\n"))
    diagonal1 = float (input ('Ingresa el valor de diagonal mayor: '))
    diagonal2 = float (input ('Ingresa el valor de diagonal menor: '))
    radio = float(input("Ingrese el radio del ciruclo: "))
           