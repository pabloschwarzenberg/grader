#Juego adivina mi número
random = __import__('random', globals(), locals(), ['randrange'], 0)
randrange = random.randrange
x = randrange(1,20)
#print(x)

intentos = 1

while intentos < 6:
    num = int(input("número: "))

    intentos = intentos + 1

    if num < x:
       print("mi número es menor")
    if num > x:
        print("mi número es mayor")
    if num == x:
        break

if num == x :
    print("Adivinaste, mi número era "+str(x)) 

if num != x:
    print("No adivinaste, mi número era "+str(x))
       


