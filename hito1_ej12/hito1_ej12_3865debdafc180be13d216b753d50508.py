#Juego adivina mi número
n_sec = 15
n_jug = 0
intentos = 5

while ((n_jug != n_sec) and (intentos > 0)):
       n_jug = eval(input("ingree numero: "))
   

    if (n_jug > n_sec):
        print(" mi numero es menor")

    elif (n_jug < n_sec):
        print("mi numero es mayor: ")

    intentos = -1

if (n_jug == n_sec):
    print("adivinaste mi numero, era:", n_sec)

else:
    if (intentos == 0):
        print("no adivinaste el numero, era:", n_sec)