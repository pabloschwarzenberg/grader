# completa el código de la función
def amigos(a,b):
  def d_a(a):
    divisores_a=0
    i=1
    for i in range(1,a+1):
      if a%i==0:
        divisores_a=divisores_a+i
        return divisores_a
      elif a%i!=0:
        return divisores_a
        break        
  def d_b(b):
    divisores_b=0
    s=1
    for s in range(1,b+1):
      if b%s==0:
        divisores_b += s
        return divisores_b
      elif b%s!=0:
        return divisores_b
        break
u = d_a(a)
w = d_b(b)

  if u==b or w==a:
    return True
  else:
    return False