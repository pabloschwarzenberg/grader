#Factores Primos
def factorizacion_de_numeros_primos(numero):
    factor_primo = 2
    while factor_primo <= numero:
        if numero % factor_primo == 0:
            print(factor_primo)
            numero = numero / factor_primo
        else:
            factor_primo += 1

numero = int(input())
factorizacion_de_numeros_primos(numero)
      