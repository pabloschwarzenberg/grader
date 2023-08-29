#Factores Primos
algo=int(input('ingresa el numero: '))
def facprimo(algo):
    abc=[]
    de=2
    f=0
    while de*de<=algo:
        while (algo%de)==0:
            abc.append(de)
            algo//=de
        de+=1
    if algo>1:
        abc.append(algo)
    while f<=len(abc)-1:
        g=abc[f]
        f=f+1
        print(g)
facprimo(algo)