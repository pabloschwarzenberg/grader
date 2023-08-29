def es_primo(numero):
    if(numero <= 1):
        return False
    if(numero <= 3):
        return True
    for i in range(2, int(numero/2)+1):
        if(numero%i == 0):
            return False
    return True

numero = int(input("Ingrese el numero: "))

factores_primos = []
while(not es_primo(numero)):
    for i in range(2, int(numero/2)+1):
        if(es_primo(i)):
            if(numero%i == 0):
                factores_primos.append(i)
                numero = int(numero / i)
                break
factores_primos.append(numero)

for i in range(len(factores_primos)):
    print(factores_primos[i])