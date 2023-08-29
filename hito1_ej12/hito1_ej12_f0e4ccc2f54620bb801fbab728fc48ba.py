#Juego adivina mi número
import random
a=random.randint(1,20)
i=int(input())
if (a!=i):
  if (a>i):
    print("El numero ingresado es menor al número secreto")
  if (a<i):
    print("El numero ingresado es mayor al número secreto")
  ii=int(input())
  if (a!=ii):
    if (a>ii):
      print("El numero ingresado es menor al número secreto")
    if (a<ii):
      print("El numero ingresado es mayor al número secreto")
    iii=int(input())
    if (a!=iii):
      if(a>iii):
        print("El numero ingresado es menor al número secreto")
      if (a<iii):
        print("El numero ingresado es mayor al número secreto")
      iv=int(input())
      if(a!=iv):
        if (a>iv):
          print("El numero ingresado es menor al número secreto")
        if (a<iv):
          print("El numero ingresado es mayor al número secreto")
        v=int(input())
        if (a!=v):
          print("No adivinaste, mi número era {}".format(a))
if (a==i) or (a==ii) or (a==iii) or (a==iv) or (a==v):
  print("Adivinaste, mi número era {}".format(a))