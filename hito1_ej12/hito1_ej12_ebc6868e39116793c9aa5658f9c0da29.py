secreto = 15 
intentos = 0
print("Intenta adivinar mi número entre 1 y 20")

while(intentos < 5):
    numero = int(input("Ingresa un número: "))
    intentos = intentos +1
    if (numero < secreto):
        print("Mi número es mayor")
    elif (numero > secreto):
        print("Mi número es menor")
    if (intentos > 5):
        print("No adivinaste, mi número era ",secreto)
if(numero != secreto and intentos <=5 ):
    print("No adivinaste, mi número era ",secreto)
else:
     (numero == secreto and intentos <=5 )
     print ("Adivinaste, mi número era ", secreto)
     