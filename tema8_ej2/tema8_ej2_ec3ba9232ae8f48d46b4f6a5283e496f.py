def buscarTodas(a,b):
    x=""
    for c in a:
      if c==b:
       x+=str(a.find(c))+" "
       z=a.find(c)
       a=list(a)
       a[z]="_"
       a=str("".join(a))
      else:
       x+=""
    return str(x)

if __name__ == "__main__":
 print(buscarTodas(input("texto o palabra:"),input("letra:")))
           