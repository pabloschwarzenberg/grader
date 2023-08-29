def buscarTodas(a,b):
  lista2=[]
  i=0
  u=0
  lista1=list(a)
  while i<len(a):
    if lista1[i]==b:
      lista2.append(str(i))
    i=i+1
  print(lista2)
  r=" ".join(lista2)
  return r

if __name__ == "__main__":
  o=str(input("Ingrese string: "))
  p=str(input("Ingrese caracter a buscar: "))
  print(buscarTodas(o,p))
           