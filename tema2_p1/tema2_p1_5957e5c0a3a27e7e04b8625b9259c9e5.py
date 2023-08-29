def es_primo(InNUm):
    if InNUm < 2:
        return False

    for num in range(2,InNUm):
        if InNUm % num == 0:
            return False

    return True

print(es_primo(12))
           