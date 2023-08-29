def buscarTodas(a,b):
    c=[]
    d=""
    f=1
    for i in(a):
      c.append(i)
    g=c.count(b)
    for i in range(len(c)):
      if c[i]==b:
        if f==g:
          d=d+str(i)
        else:
          d=d+str(i)+" "
        f=f+1    
    return(d)
        
      
    pass

if __name__=="__main__":
    a=input()
    b=input()
    print(buscarTodas(a,b))
    pass
           