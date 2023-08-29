def buscarTodas(a,b):
    c=0
    apariciones=[]
    for p in a:
      if p==b:
          apariciones.append(str(c))
      c=c+1
    apariciones2=" ".join(apariciones)
    return apariciones2
print(buscarTodas("äsfwf","f"))