n=int(input())

def purge_list(x):
    for i in range(len(x)):
        if len(x[i])!=len(x[-1]):
            x.remove(x[i])
            return purge_list(x)

    return x


def backtracking(limit,lista):
    pos=[0,1]

    if lista==[]:
        lista.append([0])
        lista.append([1])
        return backtracking(limit,lista)

    else:
        listax=[]
        y=len(lista)
        if len(lista[-1]) == (limit):
            return lista
        for x in range(0,y):
            comb=lista[x]
            for n in range(0,len(pos)):
                if n!=0:
                    comb=comb[:-1]
                comb.append(pos[n])
                lista.append(comb)
                listax.append(comb)
        lista=listax
        return backtracking(limit,lista)


x=backtracking(n,[])

for combinacion in x:
    print(combinacion)