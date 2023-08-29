import math
pi = math.pi
def area_rectangulo(base,altura):
    return base * altura
def area_triangulo(base,altura):
    return base * altura / 2
def area_rombo(diagonal1,diagonal2):
    return diagonal1 * diagonal2 / 2
def area_circulo(radio):
    return pi * (radio * radio)
if __name__=="__main__":
    print("""Area de:
1) Rectangulo
2) Triangulo
3) Rombo
4) Circulo""")
    if __name__=="__main__":
        opc = int(input("Elija una opcion: "))
        if opc == 1:
            if __name__=="__main__":
                base = int(input("Base: "))
                if __name__=="__main__":
                    altura = int(input("Altura: "))
                    if __name__=="__main__":
                        print(area_rectangulo(base,altura))
        else:
            if opc == 2:
                if __name__=="__main__":
                    base = int(input("Base: "))
                    if __name__=="__main__":
                        altura = int(input("Altura: "))
                        if __name__=="__main__":
                            print(area_triangulo(base,altura))
            else:
                if opc == 3:
                    if __name__=="__main__":
                        diagonal1 = int(input("Diagonal mayor: "))
                        if __name__=="__main__":
                            diagonal2 = int(input("Diagonal menor: "))
                            if __name__=="__main__":
                                print(area_rombo(diagonal1,diagonal2))
                else:
                    if opc == 4:
                        if __name__=="__main__":
                            radio = int(input("Radio: "))
                            if __name__=="__main__":
                                print(area_circulo(radio))
    

        
