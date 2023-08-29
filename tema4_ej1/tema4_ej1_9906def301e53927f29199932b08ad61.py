def buscarTodas(a,b):
    posicion = []
    al = list(a)
    for i in range(len(al)):
      if al[i]==b:
        posicion.append(str(i))
      else:
        None
    return (' '.join(posicion))

if __name__ == "__main__":
  a = input()
  b = input()
  buscarTodas(a,b)