def suma_divisores(a):
  divisores = []
  c=1
  while c<=a:
    if a % c==0 and a!=c:
      divisores.append(c)
    c=c+1
  if sum(divisores)== 1:
    num_primo = True
    return(sum(divisores)),(num_primo)
  else:
    num_primo = False
    return(sum(divisores)),(num_primo)