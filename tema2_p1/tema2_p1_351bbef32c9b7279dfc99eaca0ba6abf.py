def es_primo(x):
    n = int(x)
    es_primo = True
    if n == 1:
        es_primo = False
    
    for i in range(1, n):
        if n % i == 0:
            if i != 1:
                es_primo = False
                return es_primo
    return es_primo
           