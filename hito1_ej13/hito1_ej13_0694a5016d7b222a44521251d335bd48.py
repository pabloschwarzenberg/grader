#Factores Primos
def descomponer_factores(n):   
    print(n," = ", end="") 
    factor_primo = 2
    primer_factor = True
    while n>1:
        if n % factor_primo == 0:
            if primer_factor:
                primer_factor = False
            else:
                print("x", end="")
            print(factor_primo, end="")
            n //= factor_primo            
        else:  
            factor_primo += 1
n = int(input("Ingresa un número"))
descomponer_factores(n)