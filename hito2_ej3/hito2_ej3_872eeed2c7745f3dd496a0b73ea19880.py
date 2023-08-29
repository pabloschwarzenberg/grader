def adn(s,n):

    i=0

    s=s.lower()

    l=len(s)

    n=int(n)

    lista=[]

    lista2=[]

    while i<=l-n:

        a=s[i:i+n]

        if (a in lista)==False:

            lista.append(a)

            i=i+1          

        elif (a in lista)==True and (a in lista2)==False:

            lista2.append(a)

            i=i+1

        else:

            i=i+1

        

    b=0

    w=len(lista2)

    while b<w:

        q=lista2[b]

        lista.remove(q)

        b=b+1

    if lista==[]:

        return ["ninguna"]

    return lista

b=input("Inserte palabra:")

c=input("Inserte tamaño:")

r=adn(b,c)

print(r)      