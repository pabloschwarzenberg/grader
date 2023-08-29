def suma_divisores(numero):
    suma = 0
    for i in range(1, numero // 2 + 1):
        if numero % i == 0:
           suma = suma +i
    
    return suma

def numero_perfecto(a):

    return suma_divisores(a)==a