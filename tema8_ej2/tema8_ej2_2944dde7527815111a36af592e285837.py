def buscarTodas(a,b):
     t=[i for i,x in enumerate(a) if x==b]
     z=list(t)
     l=[]
     for i in z:
          l.append(str(i))
     retorna=" ".join(l)
     return retorna


if __name__ == "__main__":
     a,b=("tres tristes tigres","t")
     print(buscarTodas(a,b))

