# por favor escribe aquí tu función
#EJERCICIO 1 H1-P4

def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True            

def ejecsinprim(): #ejecsinprim= operacion para ver si el numero ingresado es primo
    numero = int(input("Porfavor, ingresa un número: "))
    resultado = es_primo(numero)

    if resultado is True:
        print("\nEl número ingresado ES primo")
    else:
        print("\nEl número ingresado NO es primo")

if __name__ == '__main__':
    ejecucsinprim()
