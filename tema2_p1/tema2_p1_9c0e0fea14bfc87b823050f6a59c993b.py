def es_primo(x):

    contador = 0

    for i in range (1, x+1):
        if x % i == 0:
            contador+=1

    if contador==2:
        return True
    else:
        return False

x = 2

print(es_primo(x))

