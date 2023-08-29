def area_triangulo(base,altura):
    x=((base*altura)/2)
    return x

def area_rectangulo(base,altura):    
    x=((base*altura))
    return x
    
def area_rombo(diagonal1,diagonal2):  
    x=((diagonal1*diagonal2)/2)
    return x
    

def area_circulo(radio):
    import math
    x=((math.pi*(radio**2)))
    return x


print("Menu")
Menu=("\n1.Area Triangulo \n2.Area rectangulo \n3.Area Rombo \n4.Area Circulo")
print(Menu)   
if __name__ == "__main__":
    Calculo=eval(input("Ingrese el area que desea calcular: "))
    if Calculo==1:
        if __name__ == "__main__":
            base=eval(input("Ingrese valor de la base: "))
            altura=eval(input("Ingrese valor de la altura: "))
        print((area_triangulo(base,altura)))
    elif Calculo==2:
        if __name__ == "__main__":
            base=eval(input("Ingrese valor de la base: "))
            altura=eval(input("Ingrese valor de la altura: "))    
        print(area_rectangulo(base,altura))
    elif Calculo==3:
        if __name__ == "__main__":
            diagonal1=eval(input("Ingrese valor de la diagonal mayor: "))
            diagonal2=eval(input("Ingrese valor de la diagonal menor: "))   
        print(area_rombo(diagonal1,diagonal2))
    elif Calculo==4:
        if __name__ == "__main__":
            radio=eval(input("Ingrese valor del radio: "))
        print(area_circulo(radio))
    pass