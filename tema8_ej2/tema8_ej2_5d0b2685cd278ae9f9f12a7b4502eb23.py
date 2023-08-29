def buscarTodas(a,b):
    contador=0
    resultado=""
    for i in a:
      if i==b:
        resultado=resultado+" "+str(contador)
      contador+=1
    resultado=resultado.strip(" ")
    return resultado

if __name__ == "__main__":
    pass
           