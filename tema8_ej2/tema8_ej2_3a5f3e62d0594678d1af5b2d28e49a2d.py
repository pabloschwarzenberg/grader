def buscarTodas(a,b):
    lista=[]
    i=0
    a=a.replace("'","")
    a.strip()
    while i<len(a):
      i=a.find(b,i)
      if i==-1:
        break
      lista.append(i)
      i=i+1
    c=""
    for j in lista:
      c=c+str(j)+" "
    c=c.strip()
    return c
      

if __name__ == "__main__":
   a=input() 
   b=input()
   print(buscarTodas(a,b))
