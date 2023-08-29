lista=[]
def binarios(n):
  if (len(lista)==n):
    return
  for a in ["1","0"]:
    lista.append(a)
    print(lista)
    if (len(lista)==n):
      print("".join(lista))
    binarios(n)
    lista.pop(-1)
   
n=int(input("escriba el largo de los numeros: "))
binarios(n)
#cada combinación que tu programa genere usando backtracking debe imprimirla en una línea separada

           