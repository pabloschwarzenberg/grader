#Juego adivina mi número
      #adivina mi numero
import random
n=random.randint(1,20)
print(n)
intentos=5
while intentos>0:
       x=int(input("numero que desea ingresar"))
       if x>n:
          print("numero mayor")
          intentos=intentos-1
       if x<n:
          print("numero menor")
          intentos=intentos-1
       if x==n:
          print("adivinaste,mi numero era",n)
          break
if intentos==0:
 print("no adivinaste, mi numero era",n)
          
