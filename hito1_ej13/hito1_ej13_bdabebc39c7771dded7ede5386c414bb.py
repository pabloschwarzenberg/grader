#Factores Primos
def descomposicion_factores_primos(numero):
    divisor = 2

    while numero > 1:
        if numero % divisor == 0:           
            numero = numero // divisor         
            print(divisor)
        else: 
            divisor += 1

numero = int(input())

descomposicion_factores_primos(numero)
      