# por favor escribe aquí tu función
def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        # Verificar si el número es divisible por algún número entre 2 y la raíz cuadrada del número
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True
           