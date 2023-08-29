import math

print("Ingrese un numero: ")

print("1.Area de Triangulo: ")

print("2.Area de Rectangulo: ")

print("3.Area de Rombo: ")

print("4.Area de Circulo: ")

a=int(input())



if a == 1:

    print("Ingrese base: ")

    base=int(input())

    print("Ingrese alutra: ")

    altura=int(input())

    area=(base*altura)/2

    print("El area es: ",area)

else:

    if a == 2:

        print("Ingrese base: ")

        base=int(input())

        print("Ingrese altura: ")

        altura=int(input())

        area=(base*altura)

        print("El area es: ",area)

    else:

        if a == 3:

            print("Ingrese diagonal mayor: ")

            dia1=int(input())

            print("Ingrese diagonal menor ")

            dia2=int(input())

            area=(dia1*dia2)/2

            print("El area es: ",area)

        else:

            print("Ingrese el radio")

            radio=int(input())

            area=math.pi*radio

            print("El area es: ",area)

