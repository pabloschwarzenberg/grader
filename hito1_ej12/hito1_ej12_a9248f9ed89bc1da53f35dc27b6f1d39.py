import random
n=random.randint(1,20)
intentos=0
while intentos<5:
   j=int(input('ingrese un numero: '))
   if n>j:
      print('tu numero ingresado es menor')
      intentos=intentos +1
   elif j>n:
      print('tu numero ingresado es mayor')
      intentos=intentos +1
   elif j==n:
      print('Adivinaste, mi número era ',n)
      break
   if intentos==5 and j!=n:
      

      print('No adivinaste, mi número era',n)
   


