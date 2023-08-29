import random
contador = 1
numero = random.randint(1,20)
print(numero)
a= int(input("ingresa el numero"))


while contador<5:
    if (a<numero):
        contador+=1
        print("tu numero es menor ")
        a = int(input("ingresa el numero"))
    if  (numero<a) :
        contador+=1
        print("tu numero es mayor")
        a = int(input("ingresa el numero"))
    if a == numero:
            contador+=5
            print ("Adivinaste, mi número era",numero)
    if contador ==5:
                print("No adivinaste, mi número era",numero)

