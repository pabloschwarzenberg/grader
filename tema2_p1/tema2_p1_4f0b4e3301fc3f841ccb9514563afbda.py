def es_primo(n):
    contador=0
    resultado=True
    for i in range(1,n+1):
        if (n%i==0):
            contador+=1
        if(contador>2) or n==1:
            resultado=False

    return resultado