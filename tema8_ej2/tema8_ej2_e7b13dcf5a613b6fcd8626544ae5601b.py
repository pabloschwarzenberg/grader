def buscarTodas(a,b):
  lista= []
  for i in range(len(a)):
    if a[i] == b:
      lista.append(i)

  return" ".join(str(v) for v in lista)



if __name__ == "__main__":
  pass
