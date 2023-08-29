def buscarTodas(a,b):
    posiciones=[]
    posicion=0
    for i in a:
      if i==b:
        posiciones.append(str(posicion))
      posicion+=1
    final=' '.join(posiciones)
    return final

if __name__ == "__main__":
    a=str(input())
    b=str(input())
    pass
           