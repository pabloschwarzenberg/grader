def es_primo(numero):
    valor = 0
    for i in range(1, numero+1):
        if numero % i == 0:
            valor = valor + 1
    if valor == 2:
        return True
    else:
        return False
numero = 10
print(es_primo(numero))


   

 