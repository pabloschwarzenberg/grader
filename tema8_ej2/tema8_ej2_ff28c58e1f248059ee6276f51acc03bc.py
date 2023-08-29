def buscarTodas(a, b):
    s = enumerate(a)
    cordenada = [i for i, y in s if y == b]
    print(cordenada)
    lista = list(cordenada)
    h = []
    for i in lista:
        h.append(str(i))
    palabr = " ".join(h)
    return palabr
    
if __name__ == "__main__":
  palabra = str(input(" ingrese palabra : "))
  letra = str(input(" ingrese la letra que quiere buscar : "))

  print(buscarTodas(palabra,letra))
           