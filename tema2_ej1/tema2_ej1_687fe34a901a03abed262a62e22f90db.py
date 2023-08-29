def opcion():

    opcion =str(input ("Ingresa una opcion, Escribe triangulo,  rectangulo ,  rombo o  circulo: "))

    if opcion == "triangulo":
        base = int(input ("Ingresa tu base: "))
        altura = int(input("ingrese altura: "))
        area_triangulo(base,altura)
        
    elif opcion == "rectangulo":
         base = int(input ("Ingresa tu base: "))
         altura = int(input("ingrese altura: "))
         area_rectangulo(base,altura)
         
    elif opcion == "rombo":
         diagonal1 = int(input ("Ingresa tu diagonal 1: "))
         diagonal2 = int(input("ingrese diagonal 2: "))
         area_rombo(diagonal1,diagonal2)
         
    elif opcion == "circulo":
        
        valor = int(input("Ingresa tu radio: "))
        area_circulo(valor)
    else:
        print ("Valor incorrecto, introduzca uno cierto")
        
def area_triangulo(base,altura):
if __name__ == "__main__":  
    area = (base*altura)/2
    print ("Tu area es : ",area)
    
def area_rectangulo(base,altura):
   
if __name__ == "__main__":   
    area = base*altura
    print("Tu area es : ",area)
   
    
def area_rombo(diagonal1,diagonal2):
if __name__ == "__main__":   
    area = (diagonal1*diagonal2)/2
    
    print("Tu area es: ",area)
    
def area_circulo(valor):
   
if __name__ == "__main__":  
   area = valor**2*3,14
   print ("Tu area es :",area)
   
   
while True:
if __name__ == "__main__":
    print("Que area deseas Calcular?: ")
    opcion()
    

           