def buscarTodas(a,b):
    a=str(a)
    at=str(a)
    b=str(b)
    i=0
    j=0
    lista=[]
    while i<len(a):
      j=at.find(b)
      if j==-1:
        break
      else:
        at=list(at)
        at[j]="*"
        lista.append(str(j))
        at="".join(at)
      i=i+1
      resultado= " ".join(lista)
      print(lista)     
    return resultado

if __name__ == "__main__":
    pass
           