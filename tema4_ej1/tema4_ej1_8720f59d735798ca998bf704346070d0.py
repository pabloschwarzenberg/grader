from random import randint
def ocultar_letras(palabra,cantidad):
    palabra=list(palabra)
    p=palabra
    i=0
    k=[]
    acumulados=[]
    while i!=cantidad:
      k=randint(0,cantidad+1)
      if p[k]=="_":
        pass
      else:
        p.pop(k)
        p.insert(k,"_")
        acumulados.append(k)
        i+=1
    p="".join(p)
    return p

def revisar_letra(palabra_secreta,palabra,letra):
    pos=[]
    p=list(palabra_secreta)
    palabra=list(palabra)
    for i in range(len(p)):
      if letra==p[i]:
        if p[i]==palabra[i]:
          pass
        else:
          palabra.pop(i)
          palabra.insert(i,letra)
    palabra="".join(palabra)
    return palabra
    

if __name__ == "__main__":
    pass
         