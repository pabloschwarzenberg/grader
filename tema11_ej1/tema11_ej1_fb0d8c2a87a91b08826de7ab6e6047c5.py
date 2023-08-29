def palindromo(palabra):
    s=0
    a=-1
    lista=0
    largo=len(palabra)
    while s<largo/2:
        if palabra[s]==palabra[a]:
            lista=1
            s+=1
            a-=1
        else:
            return False
    if lista==1:
        return True
    else:
        return False
