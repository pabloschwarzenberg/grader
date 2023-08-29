#Juego adivina mi número
      while True:
   import random
   n=random.randrange(20)#numero aleatorio de el 1-20
   numero=int(input("ingrese numero: "))
   if(n==numero):# si adivina 
       print("Ese es mi numero!")
   elif (numero != n):
    #first try
    if(numero<n):
        print("tu numero es menor!")
    if(numero>n):
      print("tu numero es mayor!")
      print("try 2")
    numero = int(input("ingrese numero: "))
#second try
    if (numero != n):
    if(numero<n):
        print("tu numero es menor!")
    if(numero>n):
        print("tu numero es mayor!")
        print("intento numero 3")
    numero = int(input("ingrese numero: "))
    if (numero != n):
    if (numero < n):
         print("mi numero es mayor!")
     if (numero > n):
        print("mi numero es menor!")
        print("intento numero 4")
     numero = int(input("ingrese numero: "))
    if (numero != n):
    if (numero < n):
        print("mi numero es mayor!")
    if (numero > n):
        print("mi numero es menor!")
        print("intento numero 5")
    numero = int(input("ingrese numero "))
    if (numero != n):
    if (numero < n):
        print("tu numero es menor")
            if (numero > n):
        print("tu numero es mayor!")
        print("