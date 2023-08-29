def suma_divisores(a):

  div=[i for i in range(1,a) if a%i==0]

  suma=sum(div)

  if suma==1:

    return suma,True

  return suma,False