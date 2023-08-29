#Juego adivina mi número
import random
numeroSecreto = random.randint(1,20) 
while True:    
    numeroUsuario = int(input('Ingrese un numero: '))
    if numeroSecreto == numeroUsuario:
        print('Adivinaste, mi numero era: ' + str(numeroSecreto))
    if numeroSecreto != numeroUsuario:
        if numeroUsuario > numeroSecreto:
            print('Mi numero es menor.')
        elif numeroUsuario < numeroSecreto:
            print('Mi numero es mayor.')
        print('Intento N°2')
        numeroUsuario = int(input('Ingrese un numero: '))
        if numeroSecreto != numeroUsuario:
            if numeroUsuario > numeroSecreto:
                print('Mi numero es menor.')
            elif numeroUsuario < numeroSecreto:
                print('Mi numero es mayor.')
            print('Intento N°3')
            numeroUsuario = int(input('Ingrese un numero: '))
            if numeroSecreto != numeroUsuario:
                if numeroUsuario > numeroSecreto:
                    print('Mi numero es menor.')
                elif numeroUsuario < numeroSecreto:
                    print('Mi numero es mayor.')
                print('Intento N°4')
                numeroUsuario = int(input('Ingrese un numero: '))
            if numeroSecreto != numeroUsuario:
                if numeroUsuario > numeroSecreto:
                    print('Mi numero es menor.')
                elif numeroUsuario < numeroSecreto:
                    print('Mi numero es mayor.')
                print('Intento N°5')
                numeroUsuario = int(input('Ingrese un numero: '))
                if numeroUsuario != numeroSecreto:
                    print('No adivinaste, mi numero era: ' + str(numeroSecreto))
                break

