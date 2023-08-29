# completa el código de la función
def suma_divisores(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True            

def app():
    num = int(input('Escribe un numero: '))
    result = suma_divisores(num)

    if result is True:
        print('El numero es primo!!')
    else:
        print('El numero no es primo!!')

if __name__ == '__main__':
    app()
  
  