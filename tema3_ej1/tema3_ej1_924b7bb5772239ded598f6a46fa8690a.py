# completa el código de la función
def suma_divisores(numero):
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    
    if suma == 1:
        return suma, True  # Retorna la suma y True si el número es primo
    else:
        return suma, False  # Retorna la suma y False si el número no es primo
           