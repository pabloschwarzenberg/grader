#Juego adivina mi número
   import random
num=random.randint(1,20)
i=1
while i<6:
    a= int(input("adivina el numero "))
    if num > a:
        print("mi numero es mayor")
    if num < a:
        print("mi numero es menor")
    if num == a:
        print("adivinaste ,ese era mi numero"+str(num))
        i=7
    i+=1
if i == 6:
    print("no adivinaste mi numero era" + str(num)) 