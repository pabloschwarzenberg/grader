def buscarTodas(a,b):
  f=""
  i=0
  c=0
  while i<len(a):
    if a.find(b)!=-1:
      if f!="":
        f+=" "
      c=str(a.find(b))
      f+=c
      a=a.replace(b,"<",1)
    i+=1
  return f

if __name__ == "__main__":
    print(buscarTodas(input(),input()))