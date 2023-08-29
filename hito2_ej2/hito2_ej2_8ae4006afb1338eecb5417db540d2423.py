def secuencia_valida(secuencia):
    for letra in secuencia:
        if not letra() in "actg":
            return False
    return True