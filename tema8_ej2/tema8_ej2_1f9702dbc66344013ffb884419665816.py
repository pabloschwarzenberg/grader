def buscarTodas(a,b):
    indices=[]
    i=0
    while i<len(a):
        if a[i]==b:
            indices.append("{}".format(i))
            indices.append(" ")
        i+=1
    indices.pop(len(indices)-1)
    stringindices="".join(indices)
    return stringindices

if __name__ == "__main__":
  a=input("Texto: ")
  b=input("Que buscar en el texto: ")
  print(buscarTodas(a,b)) 
           