# por favor escribe aquí tu función

def es_Primo(numero):
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
    numero = int(input("escriba un numero: "))
    result = es_Primo (numero)

    if result is True:
        print("el numero es primo")
    else:
        print("el numero  no es primo")
        
if __name__ == '__main__':
    app()
