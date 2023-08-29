#Juego adivina mi número
# Generar número aleatorio entre 1 y 20
num_secreto = random.randint(1, 20)

# Definir cantidad de intentos
num_intentos = 5

# Loop para 5 intentos
for i in range(num_intentos):
    # Pedir al jugador que ingrese un número
    num_ingresado = int(input("Intenta adivinar mi número (entre 1 y 20): "))
    
    # Verificar si el número ingresado es igual al número secreto
    if num_ingresado == num_secreto:
        print("Adivinaste, mi número era", num_secreto)
        break
    # Si el número ingresado es menor al número secreto indicar "mi número es mayor"
    elif num_ingresado < num_secreto:
        print("Mi número es mayor")
    # Si el número ingresado es mayor al número secreto indicar "mi número es menor"
    else:
        print("Mi número es menor")

# Si el jugador no adivina antes de que se terminen los intentos, indicar el número secreto
if num_ingresado != num_secreto:
    print("No adivinaste, mi número era", num_secreto)      