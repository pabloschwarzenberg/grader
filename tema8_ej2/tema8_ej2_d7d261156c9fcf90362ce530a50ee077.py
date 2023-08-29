def buscarTodas(a,b):
    posicion=-1
    lista=[]
    for x in a:
      if x.count(b)>0:
        posicion=a.index(b,posicion+1)
        posicion1=str(posicion)
        lista.append(posicion1)
      else:
        pass
    cadena=" ".join(lista)
    return cadena
    

if __name__ == "__main__":
    pass
           