def buscarTodas(a,b):
  fin=[i for i,x in enumerate(a) if x==b]
  seg=list(fin)
  ter=[]
  for i in seg:
    ter.append(str(i))
  result=" ".join(ter)
  return result

