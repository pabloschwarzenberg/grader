def buscarTodas(c,d):
    posicion1= c.find(d)
    p=str(posicion1)+""
    q=" "
    i=posicion1+1
    while(i<len(c)):
        if(c[i]==d):
            p=p+q+str(i)
            i=i+1
        else:
            i=i+1        
    return (p)


if __name__ == "__main__": 
  a=str(input())
  b=str(input())
  print(buscarTodas(a,b))
