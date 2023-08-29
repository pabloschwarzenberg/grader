def es_primo (num):
    primo = True
    if num!=1:
        for i in range (2, num):
            if num %i ==0:
                primo = False
    else:
        primo=False
    return primo