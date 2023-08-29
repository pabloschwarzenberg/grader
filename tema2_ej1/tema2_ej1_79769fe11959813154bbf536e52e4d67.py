from math import pi


base = ''
altura = ''
def area_triangulo(base,altura):
    
    area = base * altura
    return area / 2

radio = ''
def area_circulo(radio):
    
    longitud = radio ** 2 
    area = longitud * pi
    return area

        
diagonal1 = ''
diagonal2 = ''
def area_rombo(diagonal1,diagonal2):
    
    area = diagonal1 * diagonal2
    return area / 2

base = ''
altura = ''
def area_rectangulo(base,altura):
    
    area = base
    return area * altura       
        
def main():

    seleccion = ""
    
    print('Hola','Bienvenido')
    print(" a) Círculo")
    print(" b) Rombo")
    print(" c) Triangulo")
    print(" d) Rectangulo")
    print(" e) salir")
    
    if seleccion == 'a':
        

        area_C = area_circulo(radio)
        print('El area de tu circulo es:',area_C)
        

    elif seleccion == 'b':
        
        area_R = area_rombo(diagonal1,diagonal2)
        print('El area de tu rombo es:',area_R)
        

      
    elif seleccion == 'c':
        
        

        area_T = area_triangulo(base,altura)
        print('El area de tu triangulo es:',area_T)
        

    elif seleccion == 'd':
        
        area_Rect = area_rectangulo(base,altura)
        print('El area de tu rectangulo es:',area_Rect)
        

    elif seleccion != 'e':
        print('no existe esa alternativa intentalo nuevamente,tu has tecleado:',seleccion)
        
    else:
        print('Gracias por usar este programa')
        
        
main()  
    
    
    
    
    
        
    
                   
    

    
    




  
    
    
    
    
    
        
    
                   
    

    
    





        
    
    
    
    
    
    
        
    
                   
    

    
    




           