def es_primo(numero):
    # Verificar si el número es menor o igual a 1
    if numero <= 1:
        return False
    
    # Verificar si el número es divisible por algún número menor que él mismo
    for i in range(2, numero):
        if numero % i == 0:
            return False
    
    # Si no se encontraron divisores, el número es primo
    return True

