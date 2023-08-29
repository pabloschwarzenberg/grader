# por favor escribe aquí tu función
def es_primo(x):
    num = int(x)
    es_primo = True
    if num == 1:
        es_primo = False
    
    for i in range(1, num):
        if num % i == 0:
            if i != 1:
                es_primo = False
                return es_primo
    return es_primo
           