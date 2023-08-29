def suma_divisores(numero):
    resultado = [i for i in range(1, numero + 1) if numero % i ==0]
    return resultado
