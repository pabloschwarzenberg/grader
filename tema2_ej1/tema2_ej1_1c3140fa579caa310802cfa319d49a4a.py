import math

def area_rectangulo(base, altura):
    return base*altura

def area_triangulo(base, altura):
    return (base*altura)/2

def area_rombo(diagonal1, diagonal2):
    return (diagonal1 *diagonal2)/2

def area_circulo(radio):
    return math.pi * radio**2

if __name__ == '__main__':
	
  while(1):
    print('1. Calcular el area de un rectangulo')
    print('2. Calcular el area de un triangulo')
    print('3. Calcular el area de un rombo')
    print('4. Calcular el area de un circulo')
    print('5. Salir del programa')
    op=int(input('Ingrese una opcion:'))
    
    if op==1:
      base= float(input('Ingresa la base del rectangulo:'))
      altura= float(input('Ingresa la altura del rectangulo:'))
      area= area_rectangulo(base, altura)
      print('El area del rectangulo es', area)
      
    elif op==2:
      base=float(input('Ingresa la base del triangulo:'))
      altura=float(input('Ingresa la altura del triangulo:'))
      area=area_triangulo(base, altura)
      print('El area del triangulo es', area)
      
    elif op==3:
      diagonal1=float(input('Ingresa la diagonal 1 del rombo:'))
      diagonal2=float(input('Ingresa la diagonal 2 del rombo:'))
      area=area_rombo(diagonal1, diagonal2)
      print('El area del rombo es', area)
      
    elif op==4:
      radio=float(input('Ingrese el radio del circulo:'))
      area=areacirculo(radio)
      print('El area del circulo es', area)
      
    elif op==5:
      break
           