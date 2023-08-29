def buscarTodas(a,b):
  lista=[]
  i=0
  while i <= len(a):
    x=(a.find('b'[i:len(a)]))
    y=str(x)
    lista.append(y)
    r=" ".join(lista)
    i=i+1
  string=str(r)
  return string

if __name__ == "__main__":
  a=input()
  b=input()
           