contador = 0
try:
    numero = int(input('Introduce un número positivo: '))
    if numero < 0: 
        print('Error: Debes introducir un número entero positivo...')
    else:
        for i in range(1,numero):
            if numero % i == 0:
                contador+=i

        if numero == contador:
            print('El número',numero,'es un número perfecto.')
        else:
            print('El número',numero,'No es un número perfecto')
            

except ValueError:
    print('Error: Debes introducir un número') 