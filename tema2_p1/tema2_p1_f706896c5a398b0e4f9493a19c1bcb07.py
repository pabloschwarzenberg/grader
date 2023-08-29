# por favor escribe aquí tu función
def es_primo(numero) :
    j=2
    if numero==1 :
        return False
    for i in range(numero) :
        d=numero%j
        j+=1
        if d==0 :
            return False
        if j==numero :
            return True