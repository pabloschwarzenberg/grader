import random

numero = random.randint(1,21)

contador = 0

num_aleatorio = numero

print("ADIVINA UN NUMERO DEL 1 al 20")
print('Tienes 5 intentos para adiviniar el numero')
while num_aleatorio :
    contador += 1
    
    if contador <= 5:
        eleccion = int(input("Digite Un Numero: "))
    
        if eleccion == numero:
            print("Bien, Has acertado en el intento numero " + str(contador))
            jugando= False
            print('Adivinaste, mi número era' + str(num_aleatorio))

            break

        elif eleccion > numero:
            print('Mi numero es menor')
            
        elif eleccion < numero:
            print('Mi numero es mayor')       
    else:
        print('Se te acabaron los intentos.')
        print('No adivinaste, mi número era' + str(num_aleatorio))
        break