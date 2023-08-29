def es_primo(numero):
    if numero < 2:
        return False
    
    # Verificar divisibilidad desde 2 hasta la raíz cuadrada del número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    return True
           