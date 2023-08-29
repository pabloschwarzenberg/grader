def suma_divisores:
         for  i in range(2, n):
            if n % i == 0:
                es_primo = False
                break
            if es_primo:
                primos.append(1)

    return primos