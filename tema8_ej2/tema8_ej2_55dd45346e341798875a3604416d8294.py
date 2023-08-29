def buscarTodas(a,b):
  indices = str()
  for i in range(len(a)):
    if a[i] == b:
      indices += (str(i) + " ")
  indices = indices.strip()
  return indices

if __name__ == "__main__":
  palabra = input("Ingrese la palabra base:")
  letra = input("Ingrese la letra a buscar en la palabra base:")
  print(buscarTodas(palabra,letra))
