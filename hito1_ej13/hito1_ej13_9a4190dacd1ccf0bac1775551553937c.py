#Factores Primos
def es_primo(n):
    d=2
    primo=True
    while d<n:
        if n%d==0:
            primo=False
            break
        d=d+1
    if primo and n>1:
        return True
    else:
        return False
    
def generar_primos(maximo):
    n=2
    numeros_primos=[]
    while n<=maximo:
      if es_primo(n):
        numeros_primos.append(n)
      n=n+1
    return numeros_primos
    
l=int(input("Ingrese parametro: "))
resultado=generar_primos(l)
print(resultado)
print(len(resultado))
i=0
while i<len(resultado):
    print(resultado[i])
    i=i+1  