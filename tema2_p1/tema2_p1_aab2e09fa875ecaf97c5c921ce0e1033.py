# por favor escribe aquí tu función
def es_primo(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def app():
    num = int(input('Escriba un numero'))
    result = isPrime(num)

    if result is True:
        print('Es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    app()