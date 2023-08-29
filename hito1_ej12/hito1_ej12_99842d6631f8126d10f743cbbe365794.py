#Juego adivina mi número
from random import randint
from time import sleep

while True:
  a=int(input("Ingrese un numero"))
  shh=randint(1,20)
  if(a==shh):
      sleep(1)
      print("Adivinaste, mi número era", shh)   
  if(a!= shh):
      if(shh<a):
          print("El numero es menor")
      if(shh>a):
          print("El numero es mayor")
      print("Intento Numero 2")
      sleep(1)
      a=int(input("Ingrese un numero"))
      if(a!=shh):
          if(shh<a):
              print("El numero es menor")
          if(shh>a):
              print("El numero es mayor")
          print("Intento Numero 3")
          sleep(1)
          a=int(input("Ingrese un numero"))
          if(a!=shh):
              if(shh<a):
                  print("El numero es menor")
              if(shh>a):
                  print("El numero es mayor")
              print("Intento Numero 4")
              sleep(1)
              a=int(input("Ingrese un numero"))
              if(a!=shh):
                  if(shh<a):
                    print("El numero es menor")
                  if(shh>a):
                    print("El numero es mayor")
                  print("Intento Numero 5")
                  print("No adivinaste, mi número era ",shh)
                  sleep(1)
                  break