#Juego adivina mi número
import random
n=random.randint(1,20)
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
n5=int(input())
lista=[n1,n2,n3,n4,n5]
intento=1
i=0
while intento<=5:
    for i in lista:
        if n==i:
            print("Adivinaste, mi número era "+str(n))
            
        elif i!=n:
            if i>n:
                print("mi número es menor")
            elif i<n:
                print("mi número es mayor")
        intento+=1
                      