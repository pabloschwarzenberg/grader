def buscarTodas(a,b):
  lista = []
  for i in range(len(a)):
    if(a[i]==b):
      lista.append(i)
  return " ".join(map(str,lista))

if __name__ == "__main__":
  c = input("frase: ")
  d = input("letra: ")
  xd = buscarTodas(c,d)
  print(xd)