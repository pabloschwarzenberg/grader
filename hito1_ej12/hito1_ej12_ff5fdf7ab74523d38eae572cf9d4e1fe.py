import random
def adivina():
    n=random.randint(1,20)
    i=0
    while i<5:
        print("Intenta adivinar: ")
        intento=int(input())
        if intento>n:
            print("mi numero es menor")
            i+=1
        if intento<n:
            print ("mi numero es mayor")
            i+=1
        if intento==n:
            return("Adivinaste, mi numero era " + str(n))
    return "No adivinaste, mi numero era " + str(n)
adivina()