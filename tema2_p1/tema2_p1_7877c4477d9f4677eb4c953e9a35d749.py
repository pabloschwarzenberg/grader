def es_primo(x):
    number = int(x)
    es_primo = True
    if number==1:
        es_primo = False
    
    for i in range(1, number):
        if number%i==0:
            if i!=1:
                es_primo = False
                return es_primo
    return es_primo