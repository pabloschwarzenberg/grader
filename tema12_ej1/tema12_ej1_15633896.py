n=int(input())

def binario(n,sublista=[]):
    sublista=sublista+[]
    if len(sublista)==n:
        palabra=""
        for j in sublista:
            palabra=palabra+str(j)
        print(palabra)
        return
    else:
        for i in range(2):
            binario(n,sublista+[i])
binario(n)
