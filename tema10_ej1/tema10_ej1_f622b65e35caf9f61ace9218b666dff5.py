def mcd(a,b):
    a=int(a)
    b=int(b)
    lista=[]
    for n in range(1,max(a,b)+1):
        if (a%n==0 and b%n==0):
            lista.append(n)
    for m in range(1, len(lista)+1):
        if m>lista[0]:
            lista.insert(0,m)
    return lista[0]
    
def mcm(a,b,ab):
    a=int(a)
    b=int(b)
    ab=int(a*b)
    n=ab/mcd(a,b)
    return n

           
