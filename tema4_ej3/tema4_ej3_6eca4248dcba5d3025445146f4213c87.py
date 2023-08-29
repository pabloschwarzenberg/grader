def jerigonzo(a):
    lista=[]
    i=0
    k=0
    l=0
    m=0
    q=0
    s=0
    t=0
    while i<len(a):
        lista.append(a[i])
        i=i+1
    
    j=0

    while j<len(lista):
        if lista[j]=="a" or lista[j]=="e" or lista[j]=="i" or lista[j]=="o" or lista[j]=="u":
            lista.insert(j+1,"p")
        j=j+1

    while k<len(lista):
        if lista[k]=="p" and lista[k-1]=="a":
            lista.insert(k+1,"a")
        k=k+1

    while l<len(lista):
        if lista[l]=="p" and lista[l-1]=="e":
            lista.insert(l+1,"e")
        l=l+1

    while q<len(lista):
        if lista[q]=="p" and lista[q-1]=="i":
            lista.insert(q+1,"i")
        q=q+1
    while s<len(lista):
        if lista[s]=="p" and lista[s-1]=="o":
            lista.insert(s+1,"o")
        s=s+1
    while t<len(lista):
        if lista[t]=="p" and lista[t-1]=="u":
            lista.insert(t+1,"u")
        t=t+1
    return "".join(lista)




if __name__ == "__main__":
    pass
         