def buscarTodas(a,b):
    n=[]
    for i in range(len(a)):
      if a[i]==b:
        n.append(str(i))
    return ' '.join(n)

if __name__ == "__main__":
    pass
           