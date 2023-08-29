def buscarTodas(a,b):
    qwer=[]
    for i in range(len(a)):
      if b==a[i]:
        qwer.append(i)
    s=""
    for i in qwer:
      s+=str(i)+" "
    s=s[0:len(s)-1]
    return s

if __name__ == "__main__":
    pass
           