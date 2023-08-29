import math
p = math.pi
sol=''

def triangulo(base,altura):
    global sol
    sol=(base*altura)/2
    return sol

def rectangulo(base,altura):
    global sol
    sol=base*altura
    return sol

def rombo(diagonal1,diagonal2):
    global sol
    sol=(diagonal1*diagonal2)/2
    return sol
    
def circulo(radio):
    global sol
    sol=p*(radio**2)
    return sol

#####################
print('Bienvenido')
print('1.Calcular area de un triangulo')
print('1.Calcular area de un rectangulo')
print('1.Calcular area de un rombo')
print('1.Calcular area de un circulo')

if __name__ == "__main__":
  op=int(input('Que desea hacer?: '))
  if op==1:
    if __name__ == "__main__":
      b=int(input('Ingrese el valor de la base: '))
      a=int(input('Ingrese el valor de la altura: '))
      triangulo(b,a)
      print(sol)
      
  if op==2:
    if __name__ == "__main__":
      b=int(input('Ingrese el valor de la base: '))
      a=int(input('Ingrese el valor de la altura: '))
      rectangulo(b,a)
      print(sol)
      
  if op==3:
    if __name__ == "__main__":
      d1=int(input('Ingrese el valor de la primera diagonal: '))
      d2=int(input('Ingrese el valor de la segunda diagonal: '))
      rombo(d1,d2)
      print(sol)
 
  if op==4:
    if __name__ == "__main__":
      rad=int(input('Ingrese el valor del radio: '))
      circulo(rad)
      print(sol)
        