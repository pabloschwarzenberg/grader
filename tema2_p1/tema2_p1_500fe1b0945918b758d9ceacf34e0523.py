def es_primo(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def app():
    num = int(input('Escriba un numero: '))
    result = es_primo(num)

    if result is True:
        print('El numero ingresado es primo!!')
    else:
        print('El numero ingresado no es primo!!')

