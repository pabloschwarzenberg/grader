def buscarTodas(pal,letra):
  if pal.count(letra)==1:
   for j in list(pal):
    if j==letra:
        return pal.find(letra)
  elif pal.count(letra)>1:
    indices=[]
    contador=-1
    for j in list(pal):
     if j==letra:
        contador+=1
        indices.append(str(contador))
     elif j!=letra:
      contador+=1
    indices=" ".join(indices)
    return indices
