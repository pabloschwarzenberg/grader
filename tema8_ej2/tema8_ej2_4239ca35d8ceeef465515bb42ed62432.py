def buscarTodas(a,b):
  suma=""
  lista=[]
  for n in range(0,len(a)):
    if b==a[n]:
      suma+= str(n)+" "
  return suma.rstrip()
    

if __name__ == "__main__":
  a=input("ingrese palabra a: ")
  b=input("ingrese letra b: ")

  print(buscarTodas(a,b))