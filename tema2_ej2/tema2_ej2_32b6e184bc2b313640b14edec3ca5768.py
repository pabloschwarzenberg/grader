#FUNCIÓN QUE SUMA LOS DIVISORES DEL NÚMERO NUMERO
def calc_divis(n):
    d=1
    s=0
    while d<=n:
        if n%d==0:
            s=d+s
            d=d+1
        else:
            d+=1
    return (s)

def amigos(n1,n2):
  if n1 == n2:
    return False
  divisores1=calc_divis(n1)
  divisores2=calc_divis(n2)
  if divisores1==divisores2:
    return True
  else:
    return False
