def buscarTodas(sa,sb):
    slista=list(sa)
    slistb=list(sb)
    l=""
    for i in range(len(slista)-1):
        b=True
        while b:
              if len(slistb)==1 and slista[i]==slistb[0]:
                 l+=str(i)+" "
              b=False
              
    lo=l[:-1]     
    return lo
           