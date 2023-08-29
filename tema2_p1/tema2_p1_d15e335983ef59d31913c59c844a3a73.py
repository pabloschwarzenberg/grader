def es_primo(numero):
    if numero <= 1:
        return False
    
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

numero = 17  # Número predefinido para verificar si es primo
resultado = es_primo(numero)
print(resultado)