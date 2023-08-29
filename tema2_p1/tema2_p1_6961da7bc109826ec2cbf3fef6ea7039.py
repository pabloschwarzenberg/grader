def esPrimo(numero):
    if numero < 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True            

def app():
    numero = int(input('Escribe un número: '))
    result = esPrimo(numero)

    if result is True:
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    app() 