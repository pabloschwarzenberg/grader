def buscarTodas(a,b):
    p1=a.find(b)
    p=str(p1)+""
    q=" "
    i=p1+1
    while i<len(a):
        if a[i]==b:
          p=p+q+str(i)
          i+=1
        else:
          i+=1
    return p

if __name__ == "__main__":
    a=input()
    b=input()
              