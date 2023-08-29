def buscarTodas(a,b):
  a=list(a)
  numeros=[]
  for i in range(0,len(a)):
    if a[i]==b:
      numeros.append(str(i))
  numeros=" ".join(numeros)      
  return numeros
  pass

if __name__ == "__main__":
    pass
           