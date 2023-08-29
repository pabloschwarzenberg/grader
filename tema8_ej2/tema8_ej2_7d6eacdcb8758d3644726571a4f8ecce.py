lista = []
def buscarTodas(a,b):
    i = 0
    while i < len(a):
        a.lower()
        b.lower()
        i = a.find(b, i)
        if i == -1:
            break
        j = str(i)
        lista.append(j)
        i += 1
        k = " ".join(lista)
    return (k)

if __name__ == "__main__":
  a = input("Ingrese texto o palabra:" )
  b = input("Ingrese variable a buscar: ")
  c = buscarTodas(a,b)
  print(c)