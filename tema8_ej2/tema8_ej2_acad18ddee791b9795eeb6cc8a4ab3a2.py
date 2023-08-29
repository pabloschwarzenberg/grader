def buscarTodas(a,b):
    resp=[]
    for i in range(len(a)):
      if b == a[i]:
          resp.append(str(i))
      else:
          continue
    d=" ".join(resp)
    return d
    
          
     