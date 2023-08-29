def buscarTodas(a,b): 
    lista_a=list(a)
    pos=[]
    if b in lista_a:
        for i in range(0,len(lista_a)):
            if lista_a[i]==b:
                pos.append(str(i))
    a=""
    for e in pos:
        a+=e+" "
    a=a[:len(a)-1]
    return a

if __name__ == "__main__":
  n=input("Ingrese un string") 
  nn=input("Ingrese lo que quiere buscar")  
  print(buscarTodas(n,nn))
           