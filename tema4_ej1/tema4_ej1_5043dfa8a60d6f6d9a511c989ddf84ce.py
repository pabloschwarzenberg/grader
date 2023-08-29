from random import randint
def ocultar_letras(palabra,cantidad):
  l=[]
  p=[]
  palabra1=palabra
  for i in range (len(palabra1)):
    l.append(palabra1[i])
  for i in range(0,cantidad):
    pos=randint(1,len(palabra1)-1)
    while pos in p:
        pos=randint(1,len(palabra1)-1)
    p.append(pos)
    l[pos]="_"
  palabra=""
  for j in range(len(palabra1)):
    palabra+=l[j]
  return palabra


def revisar_letra(palabra_secreta,palabra,letra):  
    palabra0=palabra_secreta
    palabra1=palabra
    bla=list(palabra0)
    L=list(palabra)
    n=L.count(letra)
    n0=bla.count(letra)
    a=[i for i,x in enumerate(L) if x=='_']
    if letra in palabra_secreta:
        if n==n0:
            pass
        else:
            while n!=n0:
                n=L.count(letra)
                n0=bla.count(letra)
                for i in range(len(a)):
                    if letra==bla[a[i]]:
                        L[a[i]]=letra
                    print(n,n0,letra,a[i],bla[a[i]],L[a[i]],L)
    palabra=""
    for j in range(len(palabra1)):
        palabra+=L[j]
    return palabra
         