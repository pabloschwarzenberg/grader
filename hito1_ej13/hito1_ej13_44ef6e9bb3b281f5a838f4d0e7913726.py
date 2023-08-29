def es_primo(numero):
    if numero <= 1:
        return False
    elif numero == 2:
        return True
    else:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

n = int(input("Ingresa un número: "))
#listado = []
for i in range(1, n+1):
    # print(i, es_primo(i))
    if es_primo(i) and n % i == 0:
        print(i)
        #listado.append(i)
#print(listado[-1])
