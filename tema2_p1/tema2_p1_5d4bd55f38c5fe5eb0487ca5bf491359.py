# por favor escribe aquí tu función
def es_primo(n):
    contador=2
    if n<2:
        return False
    while contador<n:
        if n%contador==0:
            return False
        contador=contador+1
        return True
    if es_primo(n):
       return True
    else:
       return False
 



