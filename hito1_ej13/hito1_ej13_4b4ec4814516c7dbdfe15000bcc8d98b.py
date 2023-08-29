def es_primo(n):
    if n==1:
        return False
    elif n==2:
        return True
    elif n!=2 and n%2==0:
        return False
    
    for i in range(2,n-1):
        if n%i==0:
            return False
    return True

div=[]
def divisores(n):
    global div
    if es_primo(n)==True:
        div.append(n)
        return n
    else:
        for i in range(2,n+1):  #ir usando como el nuevo numero el cociente de la div
            if n%i==0:
                div.append(i)
                nuevo_n=n//i
                return divisores(nuevo_n)


numero=int(input('Ingrese un numero: '))
divisores(numero)
for i in div:
    print(i)