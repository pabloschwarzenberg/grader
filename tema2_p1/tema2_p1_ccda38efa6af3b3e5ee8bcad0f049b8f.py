# por favor escribe aquí tu función
n=7
def es_primo(n):
    contador=0
    for i in range(1,n+1):
        if n % i == 0:
            contador = contador + 1
    if contador==2:
        return True
    else:
        return False
print(es_primo(n))
   
           