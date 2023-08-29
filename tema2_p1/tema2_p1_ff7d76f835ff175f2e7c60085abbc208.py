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

def asdf():
    num = int(input('Escribe el numero: '))
    result = es_primo(num)

    if result is True:
        print('tu numero es primo!!')
    else:
        print('tu numero no es primo!!')

if __name__ == '__main__':
    asdf()
