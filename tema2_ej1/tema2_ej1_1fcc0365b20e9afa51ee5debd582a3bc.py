import math

if __name__ == "__main__":
    print("""Menu:
    que forma desea sacar el area:
    Triangulo
    Rectangulo
    Rombo
    Circulo""")
    forma=input("forma:")
    
    if forma =="triangulo":
        def area_triangulo(base,altura):
                base=int(input("ingrese la base:")
                altura=int(input("ingrese la altura:")
                print(base*altura)/2
                pass
    elif forma == "rectangulo":
            def area_rectangulo(base,altura):
                    base=int(input("ingrese la base:")
                    altura=int(input("ingrese la altura:")
                    print(base*altura)
                    pass
    elif forma == "rombo":
            def area_rombo(diagonal1,diagonal2):
                    diagonal1=int(input("ingrese la diagonal1:")
                    diagonal2=int(input("ingrese la diagonal2:")
                    print(diagonal1*diagonal2)/2
                    pass
    elif forma == "circulo":
            def area_circulo(radio):
                    radio=int(input("ingresa radio:")
                    print(pi*radio**2)
                    pass
