def buscarTodas(a,b):
  lista=[]
  i=0
  while i<len(a):
     if a[i]==b:
       lista.append(str(i))
       i=i+1
     else:
       i=i+1
  nueva=" ".join(lista)
  return nueva  

if __name__ == "__main__":
    pass
           