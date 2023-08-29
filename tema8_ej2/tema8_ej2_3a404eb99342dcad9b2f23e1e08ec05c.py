lista=[]
def buscarTodas(a,b):
    global x
    global y
    n=len(a)
    g=list(a)
    y=""
    for x in range(0,n):
      h=g[x]
      if h==b:
        lista.append(x)
    print(lista)
    final=" ".join(str(x) for x in lista)
    return final
      
if __name__ == "__main__":
    f=input("ingrese la frase: ")
    l=input("ingrese la letra: ")
    buscarTodas(f,l)
