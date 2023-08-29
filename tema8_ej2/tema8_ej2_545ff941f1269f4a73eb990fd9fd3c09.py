def buscarTodas(a,b):
  posiciones=[]
  for i in range(len(a)):
    if a[i]==b:
      posiciones.append(str(i))
  s = " "
  return s.join(posiciones)

if __name__ == "__main__":
    pass
           