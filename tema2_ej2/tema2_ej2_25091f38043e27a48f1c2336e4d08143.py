# completa el código de la función
def amigos(a,b):
  return
def amigos(a,b):
    if a<=0 and b<=0:
        return False
    for i in range(1,a+1):
        if a%i==0:
            divisoresa=1+a+i
    for y in range(1,b+1):
        if b%y==0:
            divisoresb=1+b+y
    if divisoresa==divisoresb:
        return True
    else:
        return False
           