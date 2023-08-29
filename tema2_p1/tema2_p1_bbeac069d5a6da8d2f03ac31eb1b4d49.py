def es_primo(n):
    i = 1
    contador = 0
    while i <= n/2:
        if n % i == 0:
            contador += 1
            i += 1
        else:
            i += 1
    if contador == 1:
        return True
    else:
        return False