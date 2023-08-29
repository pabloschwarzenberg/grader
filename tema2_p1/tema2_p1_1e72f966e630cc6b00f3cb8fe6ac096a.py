# por favor escribe aquí tu función
def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if es_primo(num) % i == 0:
                return False
        return True            

def app():
    num = int(input('Escribe un número: '))
    result = isPrime(num)

    if result is True:
        print('El número es primo!!')
    else:
        print('El número no es primo!!')

if __name__ == '__main__':
    app()