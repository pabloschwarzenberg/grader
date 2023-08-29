# por favor escribe aquí tu función
def es_primo(numero):
    if numero < 3:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True            

def app():
    numero = int(input('Ingrese un numero: '))
    result = es_primo(numero)

    if result is True:
        print('El numero es PRIMO!!')
    else:
        print('El numero NO ES PRIMO!!')

if __name__ == '__main__':
    app()