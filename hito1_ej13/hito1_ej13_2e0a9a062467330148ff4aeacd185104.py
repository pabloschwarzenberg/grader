#Factores Primos
def descomposicion_factores_primos(numero):
    
    factor_primo = 2

    
    while numero > 1:
        
        if numero % factor_primo == 0:
            
            print(factor_primo)
            
            numero = numero / factor_primo
        else:
            
            factor_primo += 1


numero = int(input("Ingrese un número entero: "))


descomposicion_factores_primos(numero) 