def buscarTodas(a,b):
  i=0
  encontradas=[]
  for letra in a:
    if letra==b:
      encontradas.append(str(i))
    i+=1
  return " " .join(encontradas)
  
#if__name__ == "__main__":
   # pass
       