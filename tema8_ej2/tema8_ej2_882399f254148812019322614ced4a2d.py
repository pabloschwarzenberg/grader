def buscarTodas(a,b):
    pass

if __name__ == "__main__":
    pass


def buscarTodas(a,b):
          m=[i for i,x in enumerate(a) if x==b]
          z=list(m)
          l=[]
          for i in z:
                    l.append(str(i))
          w=" ".join(l)
          return w
           