#Juego adivina mi número
import random
n=random.randint(1,20)
i=0
while i<=4:
    a=int(input("Ingrese número entre el 1-20:"))
    if a==n:
        print("Adivinaste, mi número era ",n)
        break
    if a>n:
        print("El número es menor.")
        i+=1
    if a<n:
        print("El número es mayor.")
        i+=1
if i==4 and a!=n:
   print("No has podido adivinar, mi número era ",n)
elif i==4 and a==n:
    print("Adivinaste, mi número era ",n)