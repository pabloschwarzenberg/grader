def buscarTodas(a,b):
    l_a=list(a)
    respuesta=[]
    for x in a:
      if x==b:
        c=a.find(x)
        d=str(a.find(x))
        respuesta.append(d)
        l_a[c]="A"
        a="".join(l_a)
      else:
        pass
      resp=" ".join(respuesta)
    return resp
if __name__ == "__main__":
    a=input()
    b=input()
    print(buscarTodas(a,b))
           