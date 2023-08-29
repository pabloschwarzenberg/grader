# por favor escribe aquí tu función
def es_primo(n):
    cant =0
    for i in range(1,n+1):
        if n%i ==0:
            cant = cant+1
    if cant == 2:
        return True
    else:
        return False
           