def buscarTodas(a,b):
     palabra = [i for i,x in enumerate(a) if x==b]
     a = list(palabra)
     l = []
     for i in a:
          l.append(str(i))
     resultado = " ".join(l)
     return resultado
if __name__ == "__main__":
    pass
           