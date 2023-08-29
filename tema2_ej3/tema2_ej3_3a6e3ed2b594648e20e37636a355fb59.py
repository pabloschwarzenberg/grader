def numero_perfecto(valor):
    numero = 0
    for ndos in range(1, valor):
        if valor % ndos == 0:
            numero = numero + ndos
    if numero == valor:
        return True
    else:
        return False


