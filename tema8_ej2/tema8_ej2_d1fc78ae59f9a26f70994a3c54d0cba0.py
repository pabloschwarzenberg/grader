def buscarTodas(a,b):
    lista_a=list(a)
    lista_c_a= list(a)
    contador=[]
    repetidos= lista_a.count(b)
    if repetidos>0:
      i=0
      for letra in lista_a:
        if letra==b:
            i2=str(i)
            contador.append(i2)
            lista_c_a.pop(i)
            i=i+1
        else:
          i=i+1
          pass
    contador=' '.join(contador)
    return contador
if __name__ == "__main__":
    pass
           