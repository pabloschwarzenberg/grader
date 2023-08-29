#Juego adivina mi número
      #4_juego adivina mi numero:
guessestaken=0
minNumero = 1
maxNumero =20

print("hola cual es tu nombre?:")
nombre=input()

numero=random.randint(minNumero,maxNumero)
  print(f"estoy empesando en un numero entre: {str(minNumero)} y {str(maxNumero)}")

while guessestaken <6:
    print("adivina el numero:")
    guess=input()
    guess=int(guess)

    guessestaken=guessestaken+1

    if guess<numero:
        print("tu numero es demasiado bajo:")
    if guess>numero:
        print("tu numero es demasiado alto:")

if guess== numero:
    guessetaken=str(guesseetaken)
    print(f"buen trabajo,{username}adivinaste mi numero,en{guessestaken}intentos")
if guess!=numero:
    numero=str(numero)
    print(f"no,el numero que estaba pensando es {number}")