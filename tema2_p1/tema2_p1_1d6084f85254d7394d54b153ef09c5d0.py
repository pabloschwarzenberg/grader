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
    num = int(input('Ingrese un Numero: '))
    result = es_primo(num)

    if result is True:
        print('El Numero es Primo!!')
    else:
        print('El Numero no Es Primo!!')

if __name__ == '__main__':
    app()
