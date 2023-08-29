def es_primo(numeroelegido):
    if numeroelegido < 2:
        return False

    for num in range(2,numeroelegido):
        if numeroelegido%num == 0:
            return False

    return True