def divisores(n):
    resultado=[]
    c=2
    while c<n:
        if n%c==0:
            resultado.append(c)
        c=c+1
    return resultado


def amigos(n,m):
  v=divisores(n)
  b=divisores(m)
  if int(sum(v))+1==m and int(sum(b))+1==n:
      return True
  else:
      return False