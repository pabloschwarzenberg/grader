def buscarTodas(a,b):
  w=[]
  j=[]
  for i in range (0,len(a)):
      if b==a[i]:
          w.append(str(i))
  for i in range (0,len(w)):
      j.append(w[i])
      j.append(" ")
  j=j[:-1]
  print(j)
  j="".join(j)
  return j
if __name__ == "__main__":
    pass
           