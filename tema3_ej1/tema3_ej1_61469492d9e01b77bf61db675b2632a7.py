# completa el código de la función
def suma_divisores(a):

  div=[i for i in range(1,a) if a%i==0]

  m=sum(div)

#  n1=print("(%d, %s)" % (m,"True"))

  #return print("(%d, %s)" % (m,"False"))

  if m==1:

    return m,True

  return m,False           