def buscarTodas(a,b):
  res = ""
  for letra in range(len(a)):
    if a[letra] == b:
      res += str(letra) + " "
  return res[:-1]