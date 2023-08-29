def es_primo(n):
        d=2
        while d<n:
            if n%d==0:
                return False
            d=d+1
        return True
    
def generar_primos(maximo):
    n=2
    numeros_primos=[]
    while n<=maximo:
        if es_primo(n):
            numeros_primos.append(n)
        n=n+1
    return numeros_primos

l=int(input("Ingrese el limite: "))
numeros=generar_primos(l)
print(numeros)
