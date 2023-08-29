ListaDePos = []

def listaAString(list1):
    return str(list1).replace('[','').replace(']','').replace(',','')

def buscarTodas(a,b):
  a = a.lower()
  b = b.lower()
  for i in range(0, len(a)):
    if a[i] == b:
      ListaDePos.append(i)
  Resultado = listaAString(ListaDePos)
  return Resultado

if __name__ == "__main__":
  pass
           