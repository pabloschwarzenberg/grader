def descomponer_factores(n):
    productoria = 1
    copia_n = n
    factor_primo = 2
    cant_factores = 0
    hay_factores = False
    while True:
        resto = copia_n % factor_primo
        if resto == 0:            
            copia_n //= factor_primo
            productoria *= factor_primo
            cant_factores += 1
        else:  
            if cant_factores > 0:
                if hay_factores:
                    print("x", end="")
                else:
                    hay_factores = True
                if cant_factores==1:
                    print(factor_primo, end="")
                else:
                    print("{:d}^{:d}".format(factor_primo, cant_factores), end="")
                cant_factores = 0
            factor_primo = siguiente_primo(factor_primo)
        if productoria == n:
            break
    if hay_factores:
        print("x", end="")
    if cant_factores==1:
        print(factor_primo, end="")
    else:
        print("{:d}^{:d}".format(factor_primo, cant_factores), end="") 