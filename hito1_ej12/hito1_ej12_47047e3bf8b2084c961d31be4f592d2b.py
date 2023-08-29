#Juego adivina mi número
n1 = int(input("escriba un numero entre 1 a 20: "))

 n = random.randint(1, 20)

 cont = 1

 while cont < 5:
    if n1 < n:
        print("mi numero es mayor")
        n1 = int(input("ingrese nuevamente: "))
        cont = cont + 1
    elif(20 > n1 > n):
        print("mi numero es menor")
        n1 = int(input("ingrese nuevamente: "))
        cont = cont + 1
    elif(n1 == n):
        print("adivinaste mi numero, era: ", n)
        break
    elif(n1 > 20):
        print("error: el numero ingresado es mayor que 20")
        break
 print("no adivinaste mi numero era", n)  
  