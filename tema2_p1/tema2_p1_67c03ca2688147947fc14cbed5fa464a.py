def es_primo(numero):
    div = []
    for i in range(1, numero + 1):
        if numero % i == 0:
            div.append(i)

    if len(div) == 2:
        if (div[0] == 1 and div[1] == numero):
            return True
    return False