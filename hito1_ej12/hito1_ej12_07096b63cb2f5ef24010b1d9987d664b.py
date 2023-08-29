#Juego adivina mi número
numerousuario= ""
numerosecreto= 26
numerointentos= 5

x = randrange(1,20)
aux = 0
while aux < 3:
    res = input("> ")
    if res == x:
        print("¡Has ganado!")
        break
    aux += 1
if aux >= 3:
    print("¡Has perdido! El número secreto era " + str(x))


      