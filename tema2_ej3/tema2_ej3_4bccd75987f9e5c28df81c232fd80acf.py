def numero_perfecto(a):
    
    lista= []
        
    for i in range(1, a):
        if (a % i == 0):
            lista.append(i)
    suma = sum(lista)
    if suma == a:
        return True
    else: return False
           