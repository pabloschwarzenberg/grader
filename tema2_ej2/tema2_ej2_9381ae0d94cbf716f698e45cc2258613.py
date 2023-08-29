# completa el código de la función
def amigos(a,b):
  x =1    
  y =1     
  suma_divisores_de_x=0
  suma_divisores_de_y=0
  while x <a:

    if a% x ==0:

      suma_divisores_de_x = x 

      print("El divisor de %d es: %d" % (a,x),"y la suma de divisores de %d es: %d" %(a,suma_divisores_de_x))

    x +=1

  while y < b:

    if b% y == 0:

      suma_divisores_de_y += y

      print("El divisor de %d es: %d" % (b, y),"y la suma de divisores de %d es: %d" %(b,suma_divisores_de_y))

    y += 1

  if suma_divisores_de_x ==b and suma_divisores_de_y ==a:

    return True

  else:

    return False

try:

 num_1 = int(input("Número a escoger 1: "))

 num_2 = int(input("Número a escoger 2: "))

 print(amigos(num_1, num_2))

except:

 print("Por favor Ingrese un Número")
