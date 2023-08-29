string=input()
n=int(input())
def subsecuencia(string,n):
    i=0
    substrings=[]
    largo_n=[]
    unicos=[]
    repetidos=[]
    u=0
    while i<len(string):
        j=0
        while j+i<len(string):
            a=string[i:i+j+1]
            a=a.lower()
            substrings.append(a)
            j=j+1
        i=i+1
    for sub in substrings:
        if len(sub)==n:
            largo_n.append(sub)
    for elemento in largo_n:
        if elemento not in unicos:
            unicos.append(elemento)
        else:
            if elemento not in repetidos:
                repetidos.append(elemento)
    l=0
    while l<len(unicos):
        elemento1=unicos[l]
        if elemento1 not in repetidos:
            l=l+1
        else:
            unicos.remove(elemento1)
    if unicos==[]:
        return["ninguna"]
    else:
        return unicos
    
print(subsecuencia(string,n))