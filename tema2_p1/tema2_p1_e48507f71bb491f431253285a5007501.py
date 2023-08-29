# por favor escribe aquí tu función
def es_primo(num):
    contador=0
    for k in range(1,num+1):
        if num%k == 0:
            contador=contador+1
    if contador==2:
        return True
    else:  
        return False