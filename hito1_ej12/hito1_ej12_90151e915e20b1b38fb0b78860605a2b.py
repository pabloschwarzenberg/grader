#Juego adivina mi número
nm = 7
n = int(input("ingresa un numero del 1 al 20 : "))

while True:
    if n<nm:
        print("mi numero es mayor")
        break
while True:
    if nm<n:
        print("mi numero es menor")
        break
while True:
    if n == nm:
        print("adivinanste, mi numero es : ")
        break