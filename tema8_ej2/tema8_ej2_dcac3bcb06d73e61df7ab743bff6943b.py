def buscarTodas(a,b):
    s=""
    for i in range(len(a)):
      if b==a[i]:
        s = s+str(i) + " "
    return s.strip()
    

if __name__ == "__main__":
    pass
           