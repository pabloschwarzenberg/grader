def buscarTodas(a,b):
  arreglo = []
  asd = ""
  for i in range(0,len(a)):
    if(a[i] == b):
      arreglo.append(i)
  for j in range(0,len(arreglo)): 
    asd = asd +" "+str(arreglo[j])
  asd = asd[1::]
  return asd

    
    

if __name__ == "__main__":
    pass
           