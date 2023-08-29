def buscarTodas(a,b):
    l=""
    a2=list(a)
    while b in a2:
      n=a2.index(b)
      a2[n]="*"
      l=l+str(n)+" " 
    l2=list(l)
    l2.pop(-1)
    l3=''.join(str(e) for e in l2)      
   
    return l3
    pass

if __name__ == "__main__":
    print(buscarTodas('tres tristes tigres','t'))
    pass
           