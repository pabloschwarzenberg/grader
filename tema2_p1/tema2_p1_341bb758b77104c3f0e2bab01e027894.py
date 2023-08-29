def es_primo(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def app():
    num = int(input('Escribe un numero: '))
    result = es_primo(num)

    if result is True:
        print('El numero es primo: ', num)
    else:
        print('El numero no es primo: ', num)
if __name__ == '__main__':
    app()