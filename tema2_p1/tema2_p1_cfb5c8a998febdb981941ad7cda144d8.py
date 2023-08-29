#Números Primos
def es_primo(n):
    if n==1:
        return False
    divisores=[]
    for i in range(2,n):
        if n%i==0:
            divisores.append(i)
    if len(divisores)==0:
        return True
    if len(divisores)!=0:
        return False
          