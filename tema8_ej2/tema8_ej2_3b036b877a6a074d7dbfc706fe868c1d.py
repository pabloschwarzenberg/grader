def buscarTodas(a,b):
  h=list(a)
  la=len(h)
  k=[]
  j=0
  while j<la:
    if h[j]==b:
        k.append(j)
    j=j+1
  k =  " ".join(str(x) for x in k)
  return(k)


if __name__ == "__main__":
  a=input("Ingresa palabra")
  b=input("Ingresa lo que buscas")
  print(buscarTodas(a,b))