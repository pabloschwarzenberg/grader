#Juego adivina mi número
import random
n=random.randint(1,20)
print(n)
n=0
X=0
I=0
while I<5:
 X=int(input("ingresa el numero: "))
 if X>n:
    print ('fallaste, el numero es mayor que la incognita')
    I=I+1
 elif X<n:
    print ('fallaste, el numero es menor que la incognita')
    I=I+1
 elif X==n:
    print ('Adivinaste, mi número era:',n)  
    break
