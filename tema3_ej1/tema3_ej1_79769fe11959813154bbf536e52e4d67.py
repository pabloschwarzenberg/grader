def suma_divisores(a):
    suma = 0
    es_primo = False

    if a != 1:
        for i in range(1,a-1):    
            if a % i == 0:
                suma = suma+i

        if suma == 1:
            es_primo = True
         
    else:
        suma = 0
             
    return suma,es_primo
    
suma_divisores(13)
 
           