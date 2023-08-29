# por favor escribe aquí tu función
def es_primo(num):
    contador=0
    for x in range(1,num+1):
        if num % x==0:
            contador +=1
    if contador ==2:
        return True
    else:
        return False
