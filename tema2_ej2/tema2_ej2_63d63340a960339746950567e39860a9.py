# completa el código de la función
def amigos(a,b):
    
    if a!=b:
        lista_a = []
        i = 1
        while a>i:
            numero2 = a//i
            if a%i == 0:
                lista_a.append(numero2)
                i += 1
            else:
                i+=1  
        i=1
        lista_b = []
        while b>i:
            numero2 = b//i
            if b%i == 0:
                lista_b.append(numero2)
                i += 1
            else:
                i+=1
        if sum(lista_b)==sum(lista_a):
            return True
        else:
            return False
    else:
        return False