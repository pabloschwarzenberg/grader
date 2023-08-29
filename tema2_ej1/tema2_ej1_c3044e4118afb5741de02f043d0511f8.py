def area_triangulo(base,altura):
    #(base x altura)/2
    r = (base * altura)/2 
    #print("el resultado es", r)
    return r
    pass

def area_rectangulo(base,altura):
    #base x altura
    r = base * altura 
    #print("el resultado es", r)
    return r
    pass

def area_rombo(diagonal1,diagonal2):
    #(diagonal1 x diagonal2)/2
    r = (diagonal1 * diagonal2)/2 
    #print("el resultado es", r)
    return r
    pass

def area_circulo(radio):
    #import math.pi 
    # pi * radio**2
    pi = 3.1415926535897932384626433832795
    #print(pi)
    r = pi * (radio**2) 
    #print("el resultado es", r) 
    #print(r)
    return r
    pass

if __name__ == "__main__":
    

    opcion = 0 

    while (not(opcion==3)):
        print("1) area de un triangulo") 
        print("2) area de un rectangulo") 
        print("3) area de un rombo")
        print("4) area de un circulo")
        print("5) Salir") 
        
        opcion = eval(input())
        
        if (opcion == 1):
            
            base = eval(input("Ingrese base: "))
            altura = eval(input("Ingrese altura: "))
            area_triangulo(base,altura)      
        
        
        if (opcion == 2):
            
            base = eval(input("Ingrese base: ")) 
            altura = eval(input("Ingrese altura: "))
            area_rectangulo(base,altura)       
        
        if (opcion == 3):
            
            diagonal1 = eval(input("Ingrese diagonal 1 ")) 
            diagonal2 = eval(input("Ingrese diagonal 2 ")) 
            area_rombo(diagonal1,diagonal2)
            
        if (opcion == 4):
            
            radio = eval(input("Ingrese radio "))
            area_circulo(radio)
             
        
        if (opcion == 5):        
            print("fin del programa")
        
        break
    pass

