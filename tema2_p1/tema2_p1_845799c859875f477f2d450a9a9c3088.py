def es_primo(numero):
    sumdiv = 0
    for n in range(1, numero+1):
        if numero % n == 0:
            sumdiv += 1
    if sumdiv == 2:
        return True
    else:
        return False

res = es_primo(6)
print(res)