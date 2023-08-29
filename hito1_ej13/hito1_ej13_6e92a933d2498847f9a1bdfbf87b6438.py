def es_primo(numero):
    if(numero==1 or numero==0):
        return False
    for i in range(2,numero):
        if numero%i==0:
            return False
            break
    return True

def factores(nro):
    lista=[]
    if es_primo(nro):
        lista.append(nro)
    else:
        aux=nro
        while(not es_primo(aux)):
            for i in range(2,aux):
                if(aux%i==0 and es_primo(i)):
                    lista.append(i)
                    aux=int(aux/i)
                    break
        lista.append(aux)        
    for i in lista:
        print(i)
cheq=int(input())
factores(cheq)
